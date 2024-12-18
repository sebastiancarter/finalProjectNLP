
with open("firstName.txt", 'r') as firstNameFile:
    firstName = firstNameFile.read()


with open("lastName.txt", 'r') as lastNameFile:
    lastName = lastNameFile.read()

with open("fullName.txt", 'w') as fullNameFile:
    print(firstName, lastName, file=fullNameFile, end="")

with open("fullName.txt", 'r') as fullNameFile:
    print(fullNameFile.read())

with open("fullName.txt", 'w') as fullNameFile:
    print(lastName, firstName, file=fullNameFile, end="")


with open("fullName.txt", 'r') as fullNameFile:
    print(fullNameFile.read())
