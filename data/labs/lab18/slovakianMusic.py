import numpy as np


with open("music_responses.txt") as inFile:
    musicList = inFile.read().strip().split(" ")

musicArray = np.array(musicList)
musicArray = musicArray.astype(np.float64)
musicPercentArray = musicArray / sum(musicArray)
musicPercentArray *= 100
print(musicPercentArray)
