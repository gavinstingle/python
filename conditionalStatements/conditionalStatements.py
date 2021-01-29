'''
This module will teach you all about conditional statements.
'''
'''
Conditional statements are (simply) statements that are True or False.
We have already been creating conditional statements:
1 == 1
2 == 2 and 3 == 3

Both of these are examples of conditional statements because we can look at
them and decide that they are either True or False.

In coding we use conditional statements with if, elif (stands for "else if"), 
and else statements to create branches in the code.

This is what it looks like:
if(conditional statement):
    #insert code
elif(conditional statement):
    #insert code
else:
    #insert code
    
Notice that there is no conditional statement with the else statement.
'''
#if is used to check a conditional statement:
#first, let's make a couple of variables to compare:
studentAnswer = "purple"
correctAnswer = "purple"

#second, let's check if the answers match:
if(studentAnswer == correctAnswer):
    #Now we are inside of the if statement
    #we know this because we have tabbed in once.
    #
    #Anything inside the if statement will run IF the conditional statement is
    #true.
    #So in this example if studentAnswer is equal to correctAnswer, then
    #we will:
    print("The student's answer is correct!")
    #print out that the student is right.
    
#Now what if we wanted the code to do something if the answer was wrong:
#We will use the same variables from before.
if(studentAnswer == correctAnswer):
    print("The student's answer is correct!")
else:
    print("The student is wrong.")
#The way this works is that else catches ANY other possibilities.
#So this will check does studentAnswer == correctAnswer. If it returns
#True, then the it will run line 46. BUT, if studentAnswer doesn't equal
#correctAnswer, then it will run line 48.

#So else is helpful when we have the user input text. Because sometimes
#users type something wrong or enter the wrong thing. So else can be used to 
#tell them that they made an incorrect choice. Let's look at an example of
#this:
userChoice = 0
if(userChoice == 1):
    print("Option 1")
else:
    print("Not an option.")
#If the user choice equals 1, then it will print option 1. else, if will print
#not an option. 

#Sometimes we have situation where we have multiple possible options, in this
#case we can use elif, to add more possible paths:
userChoice = 0

if(userChoice == 1):
    print("Option 1.")
elif(userChoice == 2):
    print("Option 2.")
elif(userChoice == 3):
    print("Option 3.")
#With elif we can add possible options. Note that there is no else statement.
#You don't need an else statement, else statements are helpful for catching
#all other possibilities.

#Now that we've seen some examples, we can point out that all you need to start
#is an if statement. Adding elif and else statements after the if statement is 
#optional and depends on what you are trying to do.

#Let's try another example:
boolean = True 
#By making this boolean True and putting it as a conditional statement, then
#we know for sure that these if statements will run.
if(boolean):
    print("First.")
if(boolean):
    print("Second.")
#If we were to run this, BOTH print statements would run. This is because the
#program will look at the First conditional statement and find True, then it
#will print the first line.
#THEN, it will look at the Second if statement and find True again. then it will
#print the second line.
#
#This means that if we write multiple IF statements one after another, they
#all have the possibility of happening.
#
#But what if we only want 1 option to happen? Let's try this:
if(boolean):
    print("First.")
elif(boolean):
    print("Second.")
#If we were to run this part, it will ONLY print line 103. This is because
#when you pair elif, and else statements with if statements ONLY one of the
#options is possible.
#
#But remember if we want multiple options to happen we can pair if statements 
#together.
#Deciding between these two options depends on the program. But it is important 
#to understand that:
#if statements paired together all have the possibility to happen
#BUT, if statements paired with elif and else statements, means that
#only one of the options will run (even if all the options are true).