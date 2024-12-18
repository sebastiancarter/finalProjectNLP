import os
import json

outPutJson = dict()
dataDir = 'data/labs'
for directory in os.listdir(dataDir):
    directory = dataDir + os.sep + directory
    if os.path.isdir(directory) and not directory.startswith('program'):
        for filename in os.listdir(directory):
            filename = directory + os.sep + filename
            if filename.endswith('.py'):
                with open(filename) as f:
                    fileContents = f.read()
                    outPutJson[directory] = outPutJson.get(directory, "") + fileContents

with open('output.json', 'w') as f:
    json.dump(outPutJson, f)





