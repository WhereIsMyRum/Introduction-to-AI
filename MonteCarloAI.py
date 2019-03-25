from random import randint
import numpy as np
from math import sqrt, log

numberOfNodes = 0
class MonteCarloAI:
    def __init__(self, numberOfSearches):
        self.totalGamesPlayed = 0
        self.numberOfSearches = numberOfSearches


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

        return gameFields, whoseTurn


    def makeDecision(self, smallFieldsArray, basesArray, whoseTurn):
        global numberOfNodes

        gameFields = self.extractGameState(smallFieldsArray, basesArray, whoseTurn)
        whoseTurn = 0
        rootNode = Node(gameFields, whoseTurn, 0, True)

        for i in range(0, self.numberOfSearches+1):
            self.expansion(rootNode, whoseTurn)

        max_games = 0
        node_to_return = 0
        for i in range(0,6):
            if(rootNode.childNodes[i] != 0):
                if(max_games < rootNode.childNodes[i].noOfGames):
                    max_games = rootNode.childNodes[i].noOfGames
                    node_to_return = i
        self.totalGamesPlayed = 0

        return node_to_return
            
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

    def expansion(self, node, whoseTurn):
        startField = 0
        endField = 6

        if(whoseTurn == 1):
            startField = 7
            endField = 13

        if(not node.expanded):
            for i in range(startField, endField):
                temp_gameState = node.gameState[:]
                if (node.gameState[i] != 0):
                    temp_gameFields, temp_whoseTurn = self.move(temp_gameState, i)
                    node.childNodes.append(Node(temp_gameFields, temp_whoseTurn, node))
                else :
                    node.childNodes.append(0)
            
            node.expanded = True
            return

        self.selection(node, whoseTurn)

    def selection(self, node, whoseTurn):
        startField = 0
        endField = 6

        if(whoseTurn == 1):
            startField = 7
            endField = 13

        node_to_simulate = self.chooseBestNode(node, startField, endField, whoseTurn)
        if (node_to_simulate == 0):
            if (node.gameState[6] + sum(node.gameState[0:5]) > 24):
                self.update(node, 1)
            elif (node.gameState[13] + sum(node.gameState[7:12]) > 24):
                self.update(node, 0)
            else:
                self.update(node,0)
            return
        if(not node_to_simulate.expanded): 
            self.expansion(node_to_simulate, whoseTurn)
            result = self.simulation(node_to_simulate.gameState, whoseTurn)
            self.update(node_to_simulate, result)
        else:
            self.expansion(node_to_simulate, whoseTurn)

    def chooseBestNode(self, node, startField, endField, whoseTurn):
        if whoseTurn == 0: 
            max_score = -1
        else:
            max_score = self.numberOfSearches

        node_to_return = 0
        for i in range(0,6):
            if(node.childNodes[i] != 0):
                if(not node.childNodes[i].explored):
                    node.childNodes[i].explored = True
                    return node.childNodes[i]
                node_score = node.childNodes[i].noOfWins / node.childNodes[i].noOfGames + 1.4 * sqrt(log(node.noOfGames)/node.childNodes[i].noOfGames)
                if (node_score > max_score and whoseTurn == 0):
                    max_score = node_score
                    node_to_return = node.childNodes[i]
                if (node_score < max_score and whoseTurn == 1):
                    max_score = node_score
                    node_to_return = node.childNodes[i]
        return node_to_return

    def simulation(self, gameState, whoseTurn):
        startField = 0
        endField = 6

        if(whoseTurn == 1):
            startField = 7
            endField = 13

        if whoseTurn == 1:
            choice = randint(startField, endField-1)
        else:
            #choice = self.prioritizeDoubleMove(gameState[:])
            choice = randint(startField, endField-1)
        temp_gameState, whoseTurn = self.move(gameState[:],choice)
        if(self.checkForGameEnd(temp_gameState)):
            if temp_gameState[6] > temp_gameState[13]:
                return 1
            else:
                return 0

        return self.simulation(temp_gameState, whoseTurn)

    def update(self, node, result):
        if (not node.rootNode):
            node.noOfGames += 1
            node.noOfWins += result
            self.update(node.parentNode, result)
        else:
            self.totalGamesPlayed += 1        

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




class Node:
    def __init__(self, gameState, whoseTurn, parentNode, rootNode = False):
        global numberOfNodes
        self.expanded = False
        self.rootNode = rootNode
        self.explored = False
        self.parentNode = parentNode
        self.whoseTurn = whoseTurn
        self.noOfWins = 0
        self.noOfGames = 0
        self.gameState = gameState[:]
        self.childNodes = []
        numberOfNodes += 1
        

