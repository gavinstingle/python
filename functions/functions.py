'''
This module will explain how to create and use functions.
'''
'''
There are a couple different parts of a function:
name - this is what the function is called and what we use to call the function
parameters - these are variables that you can send into the function
body - this is the code within the actual function (the stuff that makes it do
something). the body MUST be tabbed inside of the function
return - this is a part of the code that can return something back to where we 
called the function

Let's go over an example function that we can analyze:
'''

def addition(numOne, numTwo):
    total = numOne + numTwo
    return total

#The function above is named: addition. And it has two parameters: numOne and
#numTwo. The body of the function is from line 17-18. The return statement is
#on line 18 and returns the variable: total.
#
#If we wanted to us this function we have to CALL it. To call a function, you
#type it's name with parameters:
addition(4, 5)
#What happens is: numOne is set to 4, and numTwo is set to 5. Then total is
#calculated and set to 9. Then total is returned to where we called the
#function (line 26).
#
#In that example of calling the function we don't have anything to catch 
#what the function returned. To catch it we just need to add a variable:
var = addition(4, 5)
#Now var will be set to whatever the function returns (which will be 9). So
#if we print var:
print(var)
#It will print:
9


#Now let's try an example that doesn't return anything:

def gradeCheck(name, grade):
    if(grade >= 80):
        print(name + " is passing.")
    elif(grade < 80 and grade >= 70):
        print(name + " is on probation.")
    else:
        print(name + " is failing.")    
    return 

#The function above is named: gradeCheck. And it has two parameters: name and
#grade. The body of the function is from line 44-50. The return statement is
#on line 18 and returns nothing.
#
#Notice that we still put the return statement even if we don't return anything.
#This is so that the program knows when the function ends.
#
#If we call this function:
gradeCheck("Michael", 80)
#The program will print:
"Michael is passing."


#Now that we understand all the parts of a function, we need to ENGRAIN in our
#brain that the body of the function NEEDS to be tabbed in:
def exampleFunction():
    #This comment is inside of the funciton.
#This comment is OUTSIDE of the function.
    return
#This comment is ALSO OUTSIDE of the function.


#ADDITIONALLY, parameters are NOT REQUIRED. They just are typically in most 
#functions. This is because functions typically take data and manipulate it.