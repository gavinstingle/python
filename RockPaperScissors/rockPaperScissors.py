'''
The Objective of this program is to make a Rock, Paper, Scissors game for
the user to play against the computer. The tasks to complete are:
-There should be a loop to repeat the game. And the game should go as 
follows:
    -Welcome the user with "Welcome to Rock Paper Scissors! 
    Best two out of three. Press 'q' to quit"
    -Create variables to keep track of score
    -Begin a loop to repeat rounds until somebody wins. Someone wins
    when they have won 2 rounds. (Rounds are outlined below).
    -Once someone has won, print "Thanks for playing!", print out the final
    scores, and if the user wins: print "You win!"; if the cpu wins: print
    "CPU wins!"
    -Repeat the whole game once someone wins. And until the user chooses 
    to quit.
-A round should go as follows:
    -Have the user choose rock, paper, scissors, or q
    -Generate a random choice from the computer
    -Check the users input against the computers choice to see who won 
    the round:
        -if the user won, add one to the users score, then print out 
        the scores: "User: [#], Computer [#]"
        -else if the computer won, add one to the computers score, then
        print out the scores: "User: [#], Computer [#]"
        -else if it was a draw, print "DRAW", then print out the 
        scores: "User: [#], Computer [#]"
        -else if the user entered "q", then end the round, and the game 
        loop.
        -else the user didn't enter an accepted input, and prompt them
        to try again: "Not an option try again."
    -repeat round until someone wins.

Need to know:
.lower()
import random
random.choice(list)
break
continue

You task:
Your task is to create pseudocode for the project and then code the project
using the Objective given to you.
'''
#import random
import random

#Make a boolean variable called KeepPlaying to track whether they want to keep 
#playing and set it to True.
keepPlaying = True

#Make the game loop that continues while keepPlaying is true
while(keepPlaying):
    #Print out the welcome the user to the game
    print("Welcome to Rock Paper Scissors!")
    print("Best two out of three. Press 'q' to quit")
    
    #Make variables called userScore and cpuScore to track scores
    cpuScore = 0
    userScore = 0
    
    #Make the round loop that continues while the userScore or cpuScore is
    #less than 2
    while(userScore < 2 and cpuScore < 2):
        #Use input() to get a choice from the user (rock, paper, or scissors).
        #Store the choice in a variable.
        choice = input("Please choose(Rock, Paper, Scissors): ")
        
        #Make a list of the choices, then use random.choice() to get a 
        #random choice for the cpu. Store the choice in a variable
        choiceList = ["rock", "paper", "scissors"]
        cpuChoice = random.choice(choiceList)
        
        #Make a if/elif/else statement to check the users input against 
        #the cpu's choice:
        #NOTE: you will have to compare the users choice and the cpu choice
        #to "rock", "paper", and "scissors" separately and combine with logical
        #operators. EXAMPLE of a tie:
        '''
        if((user == "rock" and cpu == "rock") or (user == "paper" and cpu == 
            "paper") or (user == "scissors" and cpu == "scissors")):
            
            Code block
        '''
        #
        #-if the user won, add one to the users score, then print out 
        #the scores: "User: [#], Computer [#]"
        #-else if the computer won, add one to the computers score, then
        #print out the scores: "User: [#], Computer [#]"
        #-else if it was a draw, print "DRAW", then print out the 
        #scores: "User: [#], Computer [#]"
        #-else if the user entered "q", then end the round, and the game 
        #loop.
        #-else the user didn't enter an accepted input, and prompt them
        #to try again: "Not an option try again."
        if(choice.lower() == 'q'):
            keepPlaying = False
            break
        elif((choice.lower() == cpuChoice) 
             or (choice.lower() == cpuChoice)
             or (choice.lower() == cpuChoice)):
            print("DRAW")
            print("User: " + str(userScore) + " CPU: " + str(cpuScore))
        elif((choice.lower() == "rock" and cpuChoice == "scissors") 
             or (choice.lower() == "scissors" and cpuChoice == "paper")
             or (choice.lower() == "paper" and cpuChoice == "rock")):
            userScore = userScore + 1
            print("User: " + str(userScore) + " CPU: " + str(cpuScore))
        elif((choice.lower() == "rock" and cpuChoice == "paper") 
             or (choice.lower() == "scissors" and cpuChoice == "rock")
             or (choice.lower() == "paper" and cpuChoice == "scissors")):
            cpuScore = cpuScore + 1
            print("User: " + str(userScore) + " CPU: " + str(cpuScore))       
        else:
            print("Not an option try again.")

    #print out the thank you message
    print("Thanks for playing!")
    #Print out who won:
    #-if the userScore is 2, then the user won
    #-if the cpuScore is 2, then the cpu won
    if(userScore == 2):
        print("You WIN!")
    elif(cpuScore == 2):
        print("You LOSE!")
    #Print out the final scores
    print("User: " + str(userScore) + " CPU: " + str(cpuScore))