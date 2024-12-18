import csv

cocoCountDict = dict()
cocoSumDict = dict()
with open("cacao.csv") as inFile:
    reader = csv.DictReader(inFile)
    for row in reader:
        percentRange = row["Cocoa\nPercent"]
        cocoCountDict[percentRange] = cocoCountDict.get(percentRange, 0) + 1
        cocoSumDict[percentRange] = cocoSumDict.get(percentRange, 0) + float(row["Rating"])


percentRangeList = sorted(cocoCountDict)
for percentRange in percentRangeList:
    averageRating = cocoSumDict[percentRange] / cocoCountDict[percentRange]
    print(percentRange, "average rating is", averageRating)


