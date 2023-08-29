import random

def guess():
    
    myChoice = []

    color1 = (input("1st Color: ")).lower()
    color2 = (input("2nd Color: ")).lower()
    color3 = (input("3rd Color: ")).lower()
    color4 = (input("4th Color: ")).lower()

    colorChoices = [color1, color2, color3, color4]
    for i in colorChoices:
        myChoice.append(i)

    #print("Your choices: ", colorChoices)

    correctColorAndPlace, correctColorOnly = checkColourPlaces(myChoice)

    return myChoice, correctColorAndPlace, correctColorOnly

def computerRandom():
    computerChoices = []
    for i in range(4):
        randomColor = random.choice(["red", "blue", "green", "yellow", "pink", "purple", "black", "white","orange"])
        computerChoices.append(randomColor)
    
    return computerChoices


def checkWin(count, computer, me, correctColorAndPlace, correctColorOnly):
    while computer != me :
        myChoice = me
        count += 1
        correctColorAndPlace, correctColorOnly = checkColourPlaces(myChoice)

        print("Correct color in the correct place: ", correctColorAndPlace)
        print("Correct color in the wrong place: ", correctColorOnly)
        print("guesses: ", count)
        print("Try again :)")

        myChoice, correctColorAndPlace, correctColorOnly = guess()
        me = myChoice

    
    count += 1    
    print("Correct color in the correct place: ", correctColorAndPlace)
    print("Correct color in the wrong place: ", correctColorOnly)
    print("guesses: ", count)
    print("You Win!")


def checkColourPlaces(choice):
    correctColorAndPlace = 0
    correctColorOnly = 0
    myChoice = choice
    for i in myChoice:
        if i in computerChoices and (myChoice.index(i) == computerChoices.index(i)):
            correctColorAndPlace += 1
        elif i in computerChoices and (myChoice.index(i) != computerChoices.index(i)):
            correctColorOnly += 1
    
    return correctColorAndPlace, correctColorOnly


computerChoices = computerRandom()
myChoice, correctColorAndPlace, correctColorOnly = guess()



guessCount = 0
checkWin(guessCount, computerChoices, myChoice, correctColorAndPlace, correctColorOnly)


