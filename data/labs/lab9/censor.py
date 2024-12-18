# function for checking if errors are present in a sensors data
# returns the name of the sensor and true if an error is present, false if no errors
def sensorErrorChecker(sensorString):
    sensorList = sensorString.split(';')
    if "Error" in sensorList:
        return (sensorList[0], True)
    else:
        return (sensorList[0], False)



data = []
with open("sensors.txt", 'r') as inFile:
    for line in inFile:
        data.append(line)


print("the following sensors are malfunctioning:")
for sensor in data:
    name, hasError = sensorErrorChecker(sensor)
    if hasError:
        print(name)


