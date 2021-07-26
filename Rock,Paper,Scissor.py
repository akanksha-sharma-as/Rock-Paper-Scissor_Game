import random
from time import sleep
from os import system,name

def welcome():
    for i in range(22):
        print("*\t",end="")
    print()

    print("*\t",end="")
    for i in range(20):
        print(" \t",end="")
    print("*")
    print()

    print("*\t",end="")
    for i in range(20):
        print(" \t",end="")
    print("*")
    print()

    print("*\t",end="")
    for i in range(8):
        print(" \t",end="")
    print("WELCOME TO GAME KINGDOM",end="")
    for i in range(9):
        print(" \t",end="")
    print("*")
    print()

    print("*\t",end="")
    for i in range(20):
        print(" \t",end="")
    print("*")
    print()

    print("*\t",end="")
    for i in range(20):
        print(" \t",end="")
    print("*")
    print()

    for i in range(22):
        print("*\t",end="")
    print()
    print()

    input("To play press enter key....")

def clear():
    if name=='nt':
        _=system('cls')
    else:
        _=system('clear')

def menu():
    for i in range(8):
        print(" \t",end="")
    print("WELCOME TO GAME KINGDOM",end="")
    for i in range(9):
        print(" \t",end="")
    print()
    print()

    print("1. Rock, Paper and Scissor Game :)")
    print("2. Exit :(")
    player = int(input("Enter your choice : "))
    if player == 1:
        clear()
        rockGame()
    elif player == 2:
        clear()
        c=input("Do you really wanna stop playing game ?(Y/N)")
        if c=='Y':
            clear()
            print("Thanks For Coming!!")
            sleep(4)
        else:
            clear()
            menu()
    else:
        print("Invalid Input...Try Again... :)")
        sleep(4)
        clear()
        menu()

def rockGame():
    print("Hey!! Fellow Gamer!!")
    print("1. Play")
    print("2. Rules")
    print("3. Exit :(")
    c=int(input("Enter your choice : "))
    if c==1:
        clear()
        rockPlay()
    elif c==2:
        clear()
        rockRules()
    elif c==3:
        clear()
        menu()
    else:
        print("Invalid input dude!! Try Again")
        rockGame()

def rockPlay():
    
    l=["Fun","Rock","Paper","Scissor"]
    print("LETS BEGIN THE GAME !!")
    name=input("Enter your name : ")
    print("GET READY TO PLAY !!")
    sleep(4)
    clear()
    count=0
    userScore = 0
    compScore = 0
    while (userScore<5 and compScore<5 and count<25):
        count+=1
        print("ROCK, PAPER & SCISSOR GAME")
        print("Press 1. Rock")
        print("Press 2. Paper")
        print("Press 3. Scissor")
        userChoice = int(input("Enter your sword : "))
        compChoice = random.choice([1,2,3])
        print("Your choice : ",l[userChoice])
        print("Computer choice : ",l[compChoice])
        if userChoice == 1 and compChoice == 3:
            userScore+=1
        elif userChoice == 1 and compChoice == 2:
            compScore+=1
        elif userChoice == 2 and compChoice == 1:
            userScore+=1
        elif userChoice == 2 and compChoice == 3:
            compScore+=1
        elif userChoice == 3 and compChoice == 1:
            compScore+=1
        elif userChoice == 3 and compChoice ==2:
            userScore+=1
        print(name," Score = ",userScore,"Computer Score = ",compScore)
        sleep(3)
        clear()
    if userScore==5:
        print("Congratulations!! You won :)")
    elif compScore==5:
        print("Better luck next time dude :)")
    else:
        print("Good competitor...We both are of same level :)")
    sleep(5)
    menu()

def rockRules():
    print("RULES TO PLAY ROCK, PAPER & SCISSOR GAME :)")
    print("You will be playing with computer.")
    print("The following are the ways how a PLAYER 1 wins :-")
    print("\tPLAYER1 = 'Paper' and PLAYER2 ='Rock")
    print("\tPLAYER1 = 'Rock' and PLAYER2 ='Scissor")
    print("\tPLAYER1 = 'Scissor' and PLAYER2 ='Paper")
    print("\n")
    print("1. Wanna Play :)")
    print("2. Exit :(")
    c=int(input("Enter your choice : "))
    if c==1:
        clear()
        rockPlay()
    elif c==2:
        clear()
        menu()
    else:
        print("Invalid Input !!")
        sleep(4)
        rockRules()

welcome()
clear()
menu()