'''
This outline will help solidify concepts from the Functions lesson.
Fill in this outline as the instructor goes through the lesson.
'''


#1) Make a function that has two boolean parameters. If both booleans are
#true, return true. Else, return false. Then, call the function.
#Print what the function returns.
def rightOrWrong(x, y):
    if(x == True, y == True):
        return("true")
    else: 
        return("false")

x = True
y = True
answer = rightOrWrong(x, y)

print(answer)
#2) Make a function that takes one int parameter: gallons. Convert gallons
#to cups (do this by multiplying gallons by 16). Then return cups. Then,
#call the function.
#Print what the function returns.
def gallonsToCups(gallons):
    cups = gallons * 16
    return cups

print(gallonsToCups(2))

#3) Make a function of any any kind with a common SYNTAX error. Then, call the
#function.
#Print what the function returns.
def feetToYards(feet) 
    yards = feet * 3
    return yards

print(feetToYards(6))

#there is no colon after the function and function parameter in line 34