'''
In this module we will go over everything for loops.
'''
'''
Loops work the same way as if statements. Except a loop will repeat over and
over until the conditional statement is no longer true.

There are two type of loops: while and for.

The basic syntax for while loops is:
while(conditional statement):
    #do code
    
For for loops:
for [item] in [object]:
    #do code

Let's do some examples.
'''

#Let's start with while loops. And let's use a while loop to count:
x = 0
#So we make a variable that is zero.
#Then we make a loop that will run while x is less than 10. So as long as x
#is anything below 10, the loop will run.
while(x < 10):
    #Just like if statements, we tab in once to get inside of the loop
    print(x)
    #We will print out x
    x = x + 1
    #Then, we will add one to x.
    #
    #Once the code get's to the end of the loop it goes back to the start.
    #So line 36 is the last line of the loop(we know this because it's the
    #last tabbed in line. So after completing line 36 is will return to line
    #26 and check if x is still less than 10.
#Now we are out of the loop because we tabbed back once.
#Eventually, x will add to be greater then 10 and then the loop will end, and
#the program will continue.

#So loops are helpful for doing a repetitive task to data.
#Let's assume we are a teacher with 3 students:
students = [False, False, False]
#Each student is one of the items in the list. If their boolean is False
#they are failing. If their boolean is True they are passing.
#
#Now let's make a loop to go through each one and change it to True:
x = 0
while(x < len(students)):
    students[x] = True
    x = x + 1
#So the way this works is x starts at zero which is the first index.
#And the len(students) gives us the length of (the number of items in)
#students.
#So the loop will run like so, I will add line numbers so that you 
#can follow where we are, and I will write what happens on each line:
#48) x is set to 0
#49) x is less than the length of students (because 0 is less than 3) so
#we go into the loop.
#50) in students, we go to the index x (and x is 0), and we set that student
#to True.
#51) We add 1 to x making it 1.
#Now we hit the end of the loop so we repeat.
#49) x is less than the length of students (because 1 is less than 3) so
#we go into the loop.
#50) in students, we go to the index x (and x is 1), and we set that student
#to True.
#51) We add 1 to x making it 2.
#Now we hit the end of the loop so we repeat.
#49) x is less than the length of students (because 2 is less than 3) so
#we go into the loop.
#50) in students, we go to the index x (and x is 2), and we set that student
#to True.
#51) We add 1 to x making it 3.
#Now we hit the end of the loop so we repeat.
#49) x is NOT less than the length of students (because 3 is NOT less than 3) so
#we skip the loop and jump to line 52.
#
#So this is how loops work, they keep happening over and over, until the
#conditional statement is no longer True.

#Let's look at for loops and how we could do the same problem but easier:
students = [False, False, False]
#So we have our students again
for x in students:
    x = True
#This loop does the EXACT SAME thing as the last one, but this one uses a for
#loop.
#
#The way this loop works is we are saying for each item in students, do
#whatever code is inside the loop.
#And then once you are inside the loop, x is each item.
#
#So the first time we enter the loop, x is equal to students[0]
#Then, the loop assigns x (students[0]) to True.
#Then, it repeats to the next item, making x equal to students[1]
#And it repeats this process until it hits the end.

#Here's one more example of a for loop:
#This loop will add " is my name", to the end of all the
#strings in this list and then prints them out.
list = ["Michael", "Juan", "AJ"]
for x in list:
    x = x + " is my name"
    print(x)