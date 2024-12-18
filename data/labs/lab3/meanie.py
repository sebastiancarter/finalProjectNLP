
with open("firstNumber.txt", 'r') as firstNumFile:
    firstContents = firstNumFile.read()

# error handling for if firstNumber.txt doesnt have number
try:
    firstNum = float(firstContents)
except ValueError:
    print("firstNumber.txt does not contain a number")
    exit()




with open("lastNumber.txt", 'r') as lastNumFile:
    lastContents = lastNumFile.read()


# error handling for if lastNumber.txt doesnt have number
try:
    lastNum = float(lastContents)
except ValueError:
    print("lastNumber.txt does not contain a number")
    exit()


average = (firstNum + lastNum) / 2

print(average)
