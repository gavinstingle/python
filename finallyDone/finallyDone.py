def circleArea():
    radius = input("What is the radius of your circle?")
    
    pi = 3.14
    squared = int(radius) * int(radius)
    area = pi * squared 
    print("The area is: " + area)
    return area

#Leave the next line alone
circleArea()