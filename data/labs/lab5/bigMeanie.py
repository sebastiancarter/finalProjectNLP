
numberList = list()

total = 0
count = 0
with open("numbers.txt", 'r') as inFile:
    for line in inFile:
        total += float(line)
        count += 1

mean = total/count

print(mean)


