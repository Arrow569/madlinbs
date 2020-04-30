# IDE/OS: VsCode / win10 OS
# April 23, 2020
# madlibs game - practice Input and Output in Python 
# Template:
# story 1
# I enjoy practice! Ifind it helps me to --(verb)-- better
# without practice , my --(noun)-- would probably not even  work.
# my code is getting more --(adjective)-- every single day !
import string
import random
# story 2
# There once was a man who lived on a ",". He owned "," egg cups, which he holdsmost dear. One day a giant ",
# struck his home, making all the egg cups ",". His ", " egg cups were now a mess. The man was ", " around tyring to clean up. It took him hours, but he was very ",
# once he was done. He noticed that that his favorite ", " egg cupwas missing. He ran all up and down the ", " looking for it. Alas, it was nowhere to be found, and so ",
# went home with one less egg cup

# TODO: Prompt the user for parts of speech and store them in variables

# story 1
story1Words = ("Noun","Number","Noun","Verb","Adj","Verb ending in 'ing'","Adj","Adj","Noun","Name")
story2Words = ("verb","Noun","adjective")

def createStory(listOfWords):
    storedList = list(listOfWords)
    userEnter = input("Would you like to Play the Game? [Y]/[Any other button and you choose]: ")
    if userEnter == "Y" or userEnter == "Yes" or userEnter == "y":
        for i in range(0, len(listOfWords)):
            improperInput = True
            checked = True
            #storedList[i] = input("Enter a " + listOfWords[i] + ": ")
            while improperInput:
                takenInput = input("Enter a " + listOfWords[i] + ": ")
                checked = isInputOkay(takenInput)
                if checked == False:
                    print("Improper Input, Try Again.")
                else:
                    
                    #storedList[i] = takenInput
                    improperInput = False


    #print(storedList)
    return storedList
def isInputOkay(inputForList):

    if inputForList == "":
        return False
    elif inputForList in string.punctuation:
        return False
    else:
        return True

def printStory(choice, wordsGiven):
    # story1 = ("There once was a man who lived on a ",". He owned "," egg cups, which he holdsmost dear. One day a giant ",
    # " struck his home, making all the egg cups ",". His ", " egg cups were now a mess. The man was ", " around tyring to clean up. It took him hours, but he was very ",
    # " once he was done. He noticed that that his favorite ", " egg cupwas missing. He ran all up and down the ", " looking for it. Alas, it was nowhere to be found, and so ",
    # " went home with one less egg cup")
    print("------------Story-------------")
    if choice == 1:
        print("There once was a man who lived on a "+wordsGiven[0]+". He owned "+wordsGiven[1]+" egg cups, which he holds most dear. One day a giant "+wordsGiven[2]+
        " struck his home, making all the egg cups "+wordsGiven[3]+". His "+wordsGiven[4]+" egg cups were now a mess. The man was "+wordsGiven[5]+" around trying to clean up. It took him hours, but he was very "+wordsGiven[6]+
        " once he was done. He noticed that that his favorite "+wordsGiven[7]+" egg cup was missing. He ran all up and down the "+wordsGiven[8]+" looking for it. Alas, it was nowhere to be found, and so "+wordsGiven[9]+
        " went home with one less egg cup.")
        #storyChoice = list(story1)
        # story 2
        # I enjoy practice! I find it helps me to --(verb)-- better
        # without practice , my --(noun)-- would probably not even  work.
        # my code is getting more --(adjective)-- every single day !
    elif choice == 2:
        print(" I enjoy practice! I find it helps me to "+wordsGiven[0]+" better."
              "without practice , my "+wordsGiven[1]+"would probably not even  work."
              "my code is getting more" +wordsGiven[2]+" every single day !")
    else:
        print("Nothing Selected")

    print("------------------------------")


def MadGame():
    on = True
    while on:
        print("-*----------------------------*-")
        print("Madlibs! The Creative Story Game")
        print("-*----------------------------*-")
        print("Choose A Story: ")
        print(" 1) The Man and His Cups")
        print(" 2) Short and Sweet.")
        print("Q = Quit")

        choice = input("Which Story?: ")

        if choice == "1":
            choice = 1
            #createStory(story1Words)
            printStory(choice, createStory(story1Words))
        elif choice == "2":
            choice = 2
            #createStory(story1Words)
            printStory(choice, createStory(story2Words))
        elif choice == "Q" or choice == "q" or choice == "Quit" or choice == "quit":
            on = False
        else:
            print("Sorry, That isn't an option")

MadGame()
#print(story1Words)
