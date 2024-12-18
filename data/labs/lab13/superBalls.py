import random
superDict = dict()

with open("superbowl.txt", 'r') as inFile:
    for line in inFile:
        line = line.strip()
        inData = tuple(line.split(';')) # split based on ; and create a quick and easy tuple
        if len(inData) != 2: # skip unformatted entries
            continue
        
        date, teamName = inData
        year = date[-2:] # slice to get last 2 digits of date (the year)

        # quick easy string concatonation (assuming there are no entries before 1924
        # cause that was really really long ago and superbowl probably didnt exist, idk im not american)
        
        if int(year) < 24:
            year = "20" + year
        else:
            year = "19" + year

        if teamName in superDict:
            superDict[teamName].append(year)
        else:
            superDict[teamName] = [year]

for team in superDict:
    # if probability < 51.786%, print out the team
    if random.random() < 0.51786:
        print(team, "won in the following years:", superDict[team])








