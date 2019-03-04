from tkinter import *
from random import randint

root = Tk()


noOfPlayers = 2
noOfSmallFields = 6 * noOfPlayers
noOfBases = noOfPlayers
whoseTurn = randint(0,1)
print(whoseTurn)

smallFieldsArray = []
basesArray = []
buttonIDs = [0,1,2,3,4,5,6,7,8]

def disableButtons():
    val = 2 if whoseTurn == 0 else 1
    for i in range(0, 6):
        smallFieldsArray[6*val - (i+1)].config(state='disabled')
        if(smallFieldsArray[i + 6*whoseTurn]['text'] != '0'):
            smallFieldsArray[i + 6*whoseTurn].config(state='normal')

def checkIfEnd():
    counter = 0
    for i in range(0,6):
        if (smallFieldsArray[i]['text'] != '0'):
            break
        else:
            counter = counter + 1
    if (counter == 6):
        print(basesArray[1]['text'])
        for i in range(6, 12):
            basesArray[1]['text'] = str(int(basesArray[1]['text']) + int(smallFieldsArray[i]['text']))
    else:
        counter = 0
        for i in range(6,12):
            if (smallFieldsArray[i]['text'] != '0'):
                break
            else:
                counter = counter + 1
        if (counter == 6):
            print(basesArray[0]['text'])
            for i in range(0, 6):
                basesArray[0]['text'] = str(int(basesArray[0]['text']) + int(smallFieldsArray[i]['text']))
    if (counter == 6):
        for i in range(0,12):
            smallFieldsArray[i].config(state='disabled', text='0')
    
def checkSum():
    suma = 0
    for i in range(0, 12):
        suma = suma + int(smallFieldsArray[i]['text'])
    for i in range(0,2):
        suma = suma + int(basesArray[i]['text'])
    print(suma)


def buttonClick(button, buttonID):
    global whoseTurn
    value = int(button['text'])
    button.config(text="0")
    startingIndex = int(buttonID)+1
    i = int(buttonID)+1
    while (i < int(buttonID)+value+1):
        if(startingIndex == 6 and whoseTurn == 0):
            temp_value = int(basesArray[0]['text'])
            basesArray[0].config(text = str(temp_value+1))
            if (i+1 < int(buttonID)+value+1):
                temp_value = int(smallFieldsArray[startingIndex]['text'])
                smallFieldsArray[startingIndex].config(text = str(temp_value+1))
            startingIndex = startingIndex + 1
            i = i + 2
        elif(startingIndex == 12 and whoseTurn == 1):
            temp_value = int(basesArray[1]['text'])
            basesArray[1].config(text = str(temp_value+1))
            if (i+1 < int(buttonID)+value+1):
                temp_value = int(smallFieldsArray[0]['text'])
                smallFieldsArray[0].config(text = str(temp_value+1))
            i = i+2
            startingIndex = 1
        elif(startingIndex == 12):
            startingIndex = 0
        else:
            temp_value = int(smallFieldsArray[startingIndex]['text'])
            smallFieldsArray[startingIndex].config(text = str(temp_value+1))
            startingIndex = startingIndex + 1
            i = i+1
    whoseTurn = -1 * whoseTurn + 1
    disableButtons()
    checkSum()
    checkIfEnd()
    return 

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
'''
for i in range(0,noOfSmallFields):
    if (i < 4):
        smallFieldsArray.append(Button(root, text="4", height = 5,  width = 10, fg="red", command=lambda: buttonClick(buttonIDs[i])))
        smallFieldsArray[i].grid(row=0, column=i+1)
    else :
        smallFieldsArray.append(Button(root, text="4", height = 5,  width = 10, fg="green", command=lambda: buttonClick(buttonIDs[i])))
        smallFieldsArray[i].grid(row=2, column=i-3)
'''
for i in range(0, noOfBases):
    basesArray.append(Button(root, text="0", height = 10, width = 10, fg="blue", state='disabled'))

basesArray[0].grid(row=0, column=0, rowspan=3)
basesArray[1].grid(row=0, column=7, rowspan=3)




disableButtons()
root.mainloop()
