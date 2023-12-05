import numpy as np
import re
import math

with open('a5.txt', 'r') as f:
    data =  f.read()

data = data.split("\n\n")

data = [(x.split(":")[0], list(map(lambda v: v.split(" "), x.split(":")[1].strip().split("\n")))) for x in data]

dataDict = {}

for key, value in data:
    dataDict[key] = value

dataDict["seeds"] = list(map(lambda v: int(v), dataDict["seeds"][0]))

allRanges = []

def findRanges(ranges, key):
    allRanges = []
    for destination, source, length in map(int, dataDict[key]):
        newRanges = []
        while ranges:
            range = ranges.pop()
            before = (range[0],min(range[1],source))
            inter = (max(range[0], source), min(source+length, range[1]))
            after = (max(source+length, range[0]), range[1])
            if before[1]>before[0]:
                newRanges.append(before)
            if inter[1]>inter[0]:
                allRanges.append((inter[0]-source+destination, inter[1]-source+destination))
            if after[1]>after[0]:
                newRanges.append(after)
        ranges = sorted(newRanges)
    return allRanges + ranges

seedRanges = []
for i in range(0,len(dataDict["seeds"]),2):
    start, length = dataDict['seeds'][i:i+2]
    end = start + length
    seedRanges.append((start, end))


ranges = sorted(seedRanges)

dataDict.pop("seeds")

for key in list(dataDict.keys()):
    print(ranges)
    ranges = findRanges(ranges, key)

print(sorted(ranges)[0][0])