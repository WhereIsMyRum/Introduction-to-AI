from random import randint
import numpy as np

class InformedMonteCarloAI:

    def extractGameState(self, smallFieldsArray, basesArray, whoseTurn):
        gameFields_temp = []
        gameFields = []
        for i in range(0, 14):
            if i < 6:
                gameFields_temp.append(int(smallFieldsArray[i]['text']))
            elif i == 6:
                gameFields_temp.append(int(basesArray[0]['text']))
            elif i < 13:
                gameFields_temp.append(int(smallFieldsArray[i-1]['text']))
            elif i == 13:
                gameFields_temp.append(int(basesArray[1]['text']))
        if(whoseTurn == 0):
            gameFields = gameFields_temp
        else: 
            for i in range(7,14):
                gameFields.append(gameFields_temp[i])
            for i in range(0,7):
                gameFields.append(gameFields_temp[i])

        return gameFields


    def move(self, gameFields, choice):
        whoseTurn = 0
        if choice > 5:
            whoseTurn = 1
        startingIndex = choice + 1
        i = choice + 1
        value = gameFields[choice]
        gameFields[choice] = 0
        # increment correct fields
        while(i < choice+1+value):
            # skip the base of the opponent
            if(whoseTurn == 0 and startingIndex != 13):
                gameFields[startingIndex] += 1
            elif(whoseTurn == 1 and startingIndex != 6):
                gameFields[startingIndex] += 1
            else: 
                if(whoseTurn == 0):
                    startingIndex = 0
                    gameFields[startingIndex] += 1
                else:
                    startingIndex += 1
                    gameFields[startingIndex] += 1
            i += 1
            startingIndex += 1
            oppositeIndex = 5 + 2 + (7 - startingIndex-1)
            # check if a current player gets to make another move
            if(i == choice+1+value and ((whoseTurn == 0 and startingIndex-1 == 6) or (whoseTurn == 1 and startingIndex-1 == 13))):
                continue
            # check if a "steal" occures 
            elif(i == choice+1+value and gameFields[oppositeIndex] != 0 and gameFields[startingIndex-1]-1 == 0 and((whoseTurn == 0 and startingIndex-1 < 6) or (whoseTurn == 1 and startingIndex-1 > 6 and startingIndex-1 < 13))):
                if(whoseTurn == 0):
                    gameFields[6] += gameFields[oppositeIndex] + 1
                    gameFields[startingIndex-1] = 0
                    gameFields[oppositeIndex] = 0
                else :
                    gameFields[13] += gameFields[oppositeIndex] + 1
                    gameFields[startingIndex-1] = 0
                    gameFields[oppositeIndex] = 0
                whoseTurn = -1 * whoseTurn + 1
            elif(i == choice+1+value):
                whoseTurn = -1 * whoseTurn + 1
            # reset counting of field increment
            if(startingIndex == 14):
                startingIndex = 0
            # calculate game field if the end-game was reached (not sure if it works correctly) 
            if(gameFields[0] == 0 and gameFields[1] == 0 and gameFields[2] == 0 and gameFields[3] == 0 and gameFields[4] == 0 and gameFields[5] == 0):
                gameFields[13] = gameFields[13] + gameFields[7] + gameFields[8] + gameFields[9] + gameFields[10] + gameFields[11] + gameFields[12]
                for i in range(7, 13):
                    gameFields[i] = 0
                break
            
            elif(gameFields[7] == 0 and gameFields[8] == 0 and gameFields[9] == 0 and gameFields[10] == 0 and gameFields[11] == 0 and gameFields[12] == 0):
                gameFields[6] = gameFields[6] + gameFields[0] + gameFields[1] + gameFields[2] + gameFields[3] + gameFields[4] + gameFields[5]
                for i in range(0, 6):
                    gameFields[i] = 0
                break
            
        #print("Board after: ", gameFields)
        return gameFields, whoseTurn
    
    def monteCarloSearch(self, move, gameFields, whoseTurn,  numberOfAnalyzedStates, numberOfSearches):
        numberOfAnalyzedStates[0] += 1
        startingField = 0
        endingField = 6
        score = 0
        temp_gameFields = gameFields[:]
        temp_gameFields, whoseTurn = self.move(temp_gameFields, move)

        if (temp_gameFields[6] > 24 or temp_gameFields[13] > 24 or self.checkForGameEnd(temp_gameFields)):
            if (temp_gameFields[6] < 25 and temp_gameFields[13] < 25):
                if ((temp_gameFields[6] + sum(temp_gameFields[0:5])) - (temp_gameFields[13] + sum(temp_gameFields[7:12])) > 0):
                    return 1
                else:
                    return 0
            elif (temp_gameFields[6] - temp_gameFields[13] > 0):
                return 1
            else: 
                return 0
        if (whoseTurn == 1):
            startingField = 7
            endingField = 13
        
        for i in range(0, numberOfSearches):
            temp_gameFields_copy = temp_gameFields[:]
            next_move = 0
            if (whoseTurn == 1): 
                next_move = np.random.randint(startingField, endingField) 
                while (temp_gameFields_copy[next_move] == 0):
                    next_move = np.random.randint(startingField, endingField)
            else:
                next_move = self.prioritizeDoubleMove(temp_gameFields_copy) 
            score += self.monteCarloSearch(next_move, temp_gameFields_copy, whoseTurn,  numberOfAnalyzedStates, 1)
        return score

    def comparePossibleMoves(self, gameFields, whoseTurn, numberOfAnalyzedStates, numberOfSearches):
        startingField = 0
        endingField = 6
        numberOfAnalyzedStates[0] += 1
        moveScore = []
        availableMoves = []
        
        if (whoseTurn == 1):
            startingField = 7
            endingField = 13
        for i in range (startingField, endingField):
            if gameFields[i] != 0:
                availableMoves.append(i)
            else:
              availableMoves.append(0)
        for i in range(0,len(availableMoves)):
            temp_gameFields = gameFields[:]
            moveScore.append(self.monteCarloSearch(availableMoves[i], temp_gameFields, whoseTurn, numberOfAnalyzedStates, numberOfSearches))
        #printprint("Monte Carlo move score: ", moveScore)
        move = np.argmax(moveScore)
        while (gameFields[move] == 0):
            moveScore[move] = -1
            move = np.argmax(moveScore)
        #print ("monte carlo chooses: ", move)
        return availableMoves[move]

    def makeDecision(self, smallFieldsArray, basesArray, whoseTurn):
        searchtreeDepth = 0
        # extract an array of fields from the current state
        gameFields = self.extractGameState(smallFieldsArray, basesArray, whoseTurn)
        whoseTurn = 0
        # analyzed states counter
        numberOfAnalyzedStates = []
        numberOfAnalyzedStates.append(0)
        numberOfSearches = 100
        # call the function finding the most optimal move
        choice = self.comparePossibleMoves(gameFields, whoseTurn, numberOfAnalyzedStates, numberOfSearches)
        #print("Number of Analyzed states Monte-Carlo: ", numberOfAnalyzedStates)
        return choice

    def checkForGameEnd(self, gameFields):
        playerOne = True
        playerTwo = True
        for i in range(0, 6):
            if gameFields[i] > 0:
                playerOne = False

        for i in range(7, 13):
            if gameFields[i] > 0:
                playerTwo = False

        return playerOne or playerTwo

    def prioritizeDoubleMove(self, temp_gameFields_copy):
        available_double_moves = []
        for i in range(0,6):
            if (temp_gameFields_copy[i] + i == 6):
                available_double_moves.append(i)

        if (len(available_double_moves) == 0):
            return np.random.randint(0,6)
        else:
            choice = np.random.randint(0,len(available_double_moves))
            return available_double_moves[choice]




    
                


            
            

            

            
            
            