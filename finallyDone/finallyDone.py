def volumeCalculator(height, width, depth):
    area = height * width
    volume = depth * area
    sentence = "The volume of this object is: "
    print(sentence + volume)
    return volume

#Leave the next line alone
volumeCalculator(5, 5, 5)