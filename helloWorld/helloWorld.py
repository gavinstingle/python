'''
Created on Nov 6, 2020

@author: ITAUser
'''

def counting():
    x = 0
    while(x <= 100):
        print(x)
        x = x + 1
    print("DONE")
    return 

counting()

def fruits(fruit):
    for x in fruit:
        print(x)
    print("DONE")
    return 

listOFruit = ["apple", "pear", "peach", "watermelon", "tomato"]
fruits(listOFruit)

def checkStudents(studentList):
    x = 0
    while(x < len(studentList[0])):
        if(studentList[1][x] == True):
            print(studentList[0][x] + " is passing.")
        else:
            print(studentList[0][x] + " is failing.")
        x = x + 1
    print("DONE")
    return 

studentList = [["Michael", "Patrice", "Amaya", "William"], [True, True, True, False]]
checkStudents(studentList)


