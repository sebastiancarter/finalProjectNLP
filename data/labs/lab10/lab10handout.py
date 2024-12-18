def getClosest(valList, searchVal): 
    minDiff = None
    maxval = None
    for val in valList:
        currDiff = abs(searchVal - val)
        if  minDiff == None or minDiff > currDiff:
            maxVal = val
            minDiff = currDiff
    return (maxVal, minDiff)


f = open("experiment1.txt", "r")
values = []
for line in f:
    values.append(float(line))
f.close()
closestVal, difference = getClosest(values, 134.6)
print("closest value is", closestVal)

f = open("experiment2.txt", "r")
textValues = f.read().strip().split(" ")
values = []
for textValue in textValues:
    values.append(float(textValue))
print(values)
f.close()
closestVal, difference = getClosest(values, 134.6)
print("closest value is", closestVal)
