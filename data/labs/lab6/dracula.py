intList = list()
with open("integers.txt", 'r') as inFile:
    for line in inFile:
        intList.append(int(line))

for integer in intList:
    outString = ""
    for printer in range(integer):
        if printer > 9:
            outString += str(9)
        else:
            outString += str(printer)
    print(outString)

