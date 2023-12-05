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

dataDict["seeds"] = dataDict["seeds"][0]

def findMapping(key, values):
    data = dataDict[key]

    results = []
    for value in values:
        currLen = len(results)
        for x, y, z in data:
            if int(value) < int(y) + int(z) and int(y) <= int(value):
                results.append(int(x) + int(value) - int(y))
        if(len(results) == currLen):
            results.append(value)
            
    return results
results = dataDict.pop("seeds")

for key in dataDict.keys():
    results = findMapping(key, results)

print(np.min(results))
