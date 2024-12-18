data = []
with open("sensors.txt", 'r') as inFile:
    for line in inFile:
        data.append(line.split(";"))


print("the following sensors are malfunctioning:")
for sensor in data:
    if "Error" in sensor:
        print(sensor[0])


