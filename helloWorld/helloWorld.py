def poundsToGrams(pounds):
    #There are 16 ounces in one pound
    ounces = pounds * 16
    
    #There are .035 ounces in a gram
    grams = ounces / .035
    return(grams)

print(poundsToGrams(180))
print(poundsToGrams(360))