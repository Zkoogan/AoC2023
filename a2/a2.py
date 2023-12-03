import numpy as np
import re
import itertools

validationDict = {
    'green': 13,
    'blue': 14,
    'red': 12
}

keys = "|".join(validationDict.keys())

regex = rf"(\d+) ({keys})"

with open('a2.txt', 'r') as f:
    Lines = np.array(f.readlines())

def isValid(data):
    allMatches = [re.findall(regex, x) for x in data]
    isValidMask = [validationDict[x[1]] >= int(x[0]) for individualPick in allMatches for x in individualPick]
    return np.min(isValidMask) != 0

def gamePowers(data):
    allMatches = [re.findall(regex, x) for x in data]
    values = np.array(list(itertools.chain(*allMatches)))
    return np.prod([np.max(values[values[:, 1] == key][:,0].astype('uint32'), initial=1) for key in validationDict.keys()])

data = np.array([x.split(':')[1].strip() for x in Lines])

validGames = [isValid(x.split(';')) for x in data]

gamePowers = [gamePowers(x.split(';')) for x in data]
validGameNumbers = np.argwhere(validGames)+1

print(np.sum(validGameNumbers))
print(np.sum(gamePowers))
