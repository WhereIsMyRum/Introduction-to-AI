from tkinter import *
from random import randint
import GameAI 
import time


root = Tk()


noOfPlayers = 2
noOfSmallFields = 6 * noOfPlayers
noOfBases = noOfPlayers
whoseTurn = randint(0,1)
print(whoseTurn)
turn = 0

smallFieldsArray = []
basesArray = []
buttonIDs = [0,1,2,3,4,5,6,7,8]

def disableButtons():
    val = 2 if whoseTurn == 0 else 1
    for i in range(0, 6):
        smallFieldsArray[6*val - (i+1)].config(state='disabled')
        if(smallFieldsArray[i + 6*whoseTurn]['text'] != '0'):
            smallFieldsArray[i + 6*whoseTurn].config(state='normal')

# check if the game is over. If it is, transfer the remaining pebbles to the correct player
def checkIfEnd():
    counter = 0
    for i in range(0,6):
        if (smallFieldsArray[i]['text'] != '0'):
            break
        else:
            counter = counter + 1
    if (counter == 6):
        #print(basesArray[1]['text']) # print the base value before adding the remaining pebbles
        for i in range(6, 12):
            basesArray[1]['text'] = str(int(basesArray[1]['text']) + int(smallFieldsArray[i]['text']))
        return true
    else:
        counter = 0
        for i in range(6,12):
            if (smallFieldsArray[i]['text'] != '0'):
                break
            else:
                counter = counter + 1
        if (counter == 6):
            #print(basesArray[0]['text']) # print the base value before adding the remaining pebbles
            for i in range(0, 6):
                basesArray[0]['text'] = str(int(basesArray[0]['text']) + int(smallFieldsArray[i]['text']))
    if (counter == 6):
        for i in range(0,12):
            smallFieldsArray[i].config(state='disabled', text='0')
        print("Score of player 0: ", basesArray[0]['text'])
        print("Score of player 1: ", basesArray[1]['text'])
        return True

# function for checking if something hasnt been fucked up
def checkSum():
    suma = 0
    for i in range(0, 12):
        suma = suma + int(smallFieldsArray[i]['text'])
    for i in range(0,2):
        suma = suma + int(basesArray[i]['text'])
    print(suma)

def increaseButtonValue(button):
    temp_value = int(button['text'])
    button.config(text = str(temp_value+1))

    # if the field the last pebble goes into is empty, and it belongs to the player
    # that currently has his turn, check if the opposite field is not empty
    # if it is not empty, then steal the pebbles
def checkForEmptyField(button, buttonIndex):
    temp_value = int(button['text'])
    oppositeFieldIndex = 5 + 1 + (5 - buttonIndex)
    temp_opposite_value = int(smallFieldsArray[oppositeFieldIndex]['text'])
    if (temp_value == 0 and temp_opposite_value != 0):
        for  i in range(0,  temp_opposite_value +1 ):
            increaseButtonValue(basesArray[whoseTurn])
        smallFieldsArray[oppositeFieldIndex].config(text = "0")
        #print('last was zero and opposite not empty! Stealing pebbles from ', oppositeFieldIndex)
    else:
        increaseButtonValue(button)


def buttonClick(button, buttonID):

    global whoseTurn
    value = int(button['text'])
    button.config(text="0")
    startingIndex = int(buttonID)+1
    i = int(buttonID)+1

    while (i < int(buttonID)+value+1):
        # check if the points need to be inserted into left base
        if(startingIndex == 6 and whoseTurn == 0):
            increaseButtonValue(basesArray[0])
            # check if the point inserted into the base was the last pebble.
            # if so, give the same  player another turn (else instruction)
            if (i+1 < int(buttonID)+value+1):
                increaseButtonValue(smallFieldsArray[startingIndex])
            else:
                whoseTurn = -1 * whoseTurn + 1
            startingIndex = startingIndex + 1
            i = i + 2
        # check if the points need to be inserted into rigth base
        elif(startingIndex == 12 and whoseTurn == 1):
            increaseButtonValue(basesArray[1])
            # check if the point inserted into the base was the last pebble.
            # if so, give the same  player another turn (else instruction)
            if (i+1 < int(buttonID)+value+1):
                increaseButtonValue(smallFieldsArray[0])
            else:
                whoseTurn = -1 * whoseTurn + 1
            i = i+2
            startingIndex = 1
        # reset counting at the right side
        elif(startingIndex == 12):
            startingIndex = 0

        else:
            if( i+1 == int(buttonID)+value+1 and (startingIndex < 6 and whoseTurn == 0 or startingIndex > 5 and whoseTurn == 1)):
                    checkForEmptyField(smallFieldsArray[startingIndex], startingIndex)

            else:
                increaseButtonValue(smallFieldsArray[startingIndex])
            startingIndex = startingIndex + 1
            i = i+1

    whoseTurn = -1 * whoseTurn + 1
    disableButtons()
    checkSum()
    if(checkIfEnd()):
        print("End of game")
        exit()
    return 

def setupBoard():
    smallFieldsArray.append(Button(root, text="4", height = 5,  width = 10, fg="red", command=lambda: buttonClick(smallFieldsArray[0], 0)))
    smallFieldsArray[0].grid(row=0, column=5+1)
    smallFieldsArray.append(Button(root, text="4", height = 5,  width = 10, fg="red", command=lambda: buttonClick(smallFieldsArray[1], 1)))
    smallFieldsArray[1].grid(row=0, column=4+1)
    smallFieldsArray.append(Button(root, text="4", height = 5,  width = 10, fg="red", command=lambda: buttonClick(smallFieldsArray[2], 2)))
    smallFieldsArray[2].grid(row=0, column=3+1)
    smallFieldsArray.append(Button(root, text="4", height = 5,  width = 10, fg="red", command=lambda: buttonClick(smallFieldsArray[3], 3)))
    smallFieldsArray[3].grid(row=0, column=2+1)
    smallFieldsArray.append(Button(root, text="4", height = 5,  width = 10, fg="red", command=lambda: buttonClick(smallFieldsArray[4], 4)))
    smallFieldsArray[4].grid(row=0, column=1+1)
    smallFieldsArray.append(Button(root, text="4", height = 5,  width = 10, fg="red", command=lambda: buttonClick(smallFieldsArray[5], 5)))
    smallFieldsArray[5].grid(row=0, column=0+1)
    smallFieldsArray.append(Button(root, text="4", height = 5,  width = 10, fg="green", command=lambda: buttonClick(smallFieldsArray[6], 6)))
    smallFieldsArray[6].grid(row=2, column=4-3)
    smallFieldsArray.append(Button(root, text="4", height = 5,  width = 10, fg="green", command=lambda: buttonClick(smallFieldsArray[7], 7)))
    smallFieldsArray[7].grid(row=2, column=5-3)
    smallFieldsArray.append(Button(root, text="4", height = 5,  width = 10, fg="green", command=lambda: buttonClick(smallFieldsArray[8], 8)))
    smallFieldsArray[8].grid(row=2, column=6-3)
    smallFieldsArray.append(Button(root, text="4", height = 5,  width = 10, fg="green", command=lambda: buttonClick(smallFieldsArray[9], 9)))
    smallFieldsArray[9].grid(row=2, column=7-3)
    smallFieldsArray.append(Button(root, text="4", height = 5,  width = 10, fg="green", command=lambda: buttonClick(smallFieldsArray[10], 10)))
    smallFieldsArray[10].grid(row=2, column=8-3)
    smallFieldsArray.append(Button(root, text="4", height = 5,  width = 10, fg="green", command=lambda: buttonClick(smallFieldsArray[11], 11)))
    smallFieldsArray[11].grid(row=2, column=9-3)
    for i in range(0, noOfBases):
        basesArray.append(Button(root, text="0", height = 10, width = 10, fg="blue", state='disabled'))
    basesArray[0].grid(row=0, column=0, rowspan=3)
    basesArray[1].grid(row=0, column=7, rowspan=3)
'''
for i in range(0,noOfSmallFields):
    if (i < 4):
        smallFieldsArray.append(Button(root, text="4", height = 5,  width = 10, fg="red", command=lambda: buttonClick(buttonIDs[i])))
        smallFieldsArray[i].grid(row=0, column=i+1)
    else :
        smallFieldsArray.append(Button(root, text="4", height = 5,  width = 10, fg="green", command=lambda: buttonClick(buttonIDs[i])))
        smallFieldsArray[i].grid(row=2, column=i-3)
'''



## start the game
setupBoard()
disableButtons()
AI = GameAI.AI()

printed = 0
while True:
    root.update_idletasks()
    root.update()
    if(whoseTurn == 0):
        choice = AI.makeDecision(smallFieldsArray, basesArray)
        print("turn: ", turn)
        print("AI clicking: ", choice) 
        buttonClick(smallFieldsArray[choice], choice)
        turn += 1
        printed = 0
    if (whoseTurn == 1 and printed == 0):
        print("-----------next turn: ", whoseTurn, " -------------")
        printed = 1

