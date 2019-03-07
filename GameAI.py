from random import randint
import numpy as np
class AI:

    def extractGameState(self, smallFieldsArray, basesArray):
        gameFields = []

        for i in range(0, 14):
            if i < 6:
                gameFields.append(int(smallFieldsArray[i]['text']))
            elif i == 6:
                gameFields.append(int(basesArray[0]['text']))
            elif i < 13:
                gameFields.append(int(smallFieldsArray[i-1]['text']))
            elif i == 13:
                gameFields.append(int(basesArray[1]['text']))

        return gameFields

    def movePrototype(self, gameFields, choice):
        whoseTurn = 0
        if choice > 5:
            whoseTurn = 1
        #print("Turn of player: ", whoseTurn, "choice: ", choice)
        #print("Board before: ", gameFields)
        startingIndex = choice + 1
        i = choice + 1
        value = gameFields[choice]
        gameFields[choice] = 0
        while(i < choice+1+value):
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
            #if(i == choice+1+value and whoseTurn == 0 and startingIndex-1 < 6) : 
                #print("Starting index: ", gameFields[startingIndex-1] - 1, " opposite index: ", gameFields[oppositeIndex])
            if(i == choice+1+value and ((whoseTurn == 0 and startingIndex-1 == 6) or (whoseTurn == 1 and startingIndex-1 == 13))):
                whoseTurn = whoseTurn
            elif(i == choice+1+value and gameFields[oppositeIndex] != 0 and gameFields[startingIndex-1]-1 == 0 and((whoseTurn == 0 and startingIndex-1 < 6) or (whoseTurn == 1 and startingIndex-1 > 6 and startingIndex-1 < 13))):
                #print("Whose turn: ", whoseTurn, " Starting index: ", startingIndex, " Opposite index: ", oppositeIndex)
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

            if(startingIndex == 14):
                startingIndex = 0

        #print("Board after: ", gameFields)
        return gameFields, whoseTurn




    def move(self, gameFields, i):
        if i < 6: 
            return gameFields, 1
        else:
            return gameFields, 0
        

    def findBestMove(self, gameFields, whoseTurn, searchtreeDepth):
        noOfAvailableMoves = 6 # actually it is 6 as there are 6 fields that can be choosen, but this is to be used to iterate over fields
        moveScore = []
        startingField = 0
        endingField = 6
        temp_gameFields = gameFields[:]
        whoseTurnAtCurrentDepth = whoseTurn
        if (whoseTurn == 1):
            startingField = 7
            endingField = 13

        if(searchtreeDepth == 5):
            #print("At search tree depth 3 the score is: ", base[0], " ", base[1])
            #print("Depth 2, board: ",  gameFields)
            #print("Score: ", temp_gameFields[6] - temp_gameFields[13])
            return temp_gameFields[6] - temp_gameFields[13]
        else:
            for i in range(startingField, endingField):
                temp_gameFields = gameFields[:]
                if(temp_gameFields[i] == 0):
                    moveScore.append(temp_gameFields[6] - temp_gameFields[13])
                    continue
                else:
                    #print("turn of player: ", whoseTurn, " choosing field: ", i)
                    temp_gameFields, whoseTurn = self.movePrototype(temp_gameFields, i)
                    
                    moveScore.append(self.findBestMove(temp_gameFields, whoseTurn, searchtreeDepth+1))
                    whoseTurn = -1 * whoseTurn + 1
        
        if searchtreeDepth == 0:
            maxScore = np.argmax(moveScore)
            while(gameFields[maxScore] == 0):
                moveScore[maxScore] = -100
                maxScore = np.argmax(moveScore)
            print(moveScore)
            return maxScore
        if(whoseTurnAtCurrentDepth == 0):
            #print("At search tree depth: ", searchtreeDepth,  " the move score is: ",  moveScore, ". Choosing max: ", max(moveScore))
           #print("Depth(max node): ", searchtreeDepth, " score: ", moveScore)
            return max(moveScore)
        if(whoseTurnAtCurrentDepth == 1):
            #print("At search tree depth: ", searchtreeDepth,  " the move score is: ",  moveScore, ". Choosing max: ", max(moveScore))
            #print("Depth(max node): ", searchtreeDepth, " score: ", moveScore)
            return min(moveScore)

    def makeDecision(self, smallFieldsArray, basesArray):
        searchtreeDepth = 0
        whoseTurn = 0
        gameFields = self.extractGameState(smallFieldsArray, basesArray)
        
        
        choice = self.findBestMove(gameFields, whoseTurn, searchtreeDepth)
        #print(gameFields)
        return choice

    


        
            