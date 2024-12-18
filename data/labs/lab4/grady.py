with open("studentScore.txt", 'r') as inFile:
    grade = inFile.read()


try:
    grade = float(grade)
except ValueError:
    print("file had invalid contents")
    exit(1)

# I think this is reasonable, 97 should give you a pass I think
if grade >= 97 and grade <= 100:
    print("The student passed with score", grade)
elif grade < 97 and grade >= 0:
    print("The student failed with score", grade)
else:
    print("error, the score", grade, " is out of range")


