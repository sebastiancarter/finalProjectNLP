newDict = dict() # alternative and much better way of declaring a dict

f = open("conversions.txt", "r")
for line in f:
    tokens = line.strip().split(" ")
    unit = tokens[0]
    convFactor = float(tokens[1])
    newDict[unit] = convFactor
    
f.close()

f = open("measurements.txt", "r")
for line in f:
    tokens = line.strip().split(" ")
    amount = float(tokens[0])
    chosenUnit = tokens[1]
    if chosenUnit == "centimeters":
        print(amount, chosenUnit)
    else:
        try:
            print((newDict[chosenUnit]*amount), "centimeters")
        except KeyError:
            print("unknown unit", chosenUnit)

f.close()
