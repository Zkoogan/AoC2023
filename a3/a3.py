import numpy as np
import re

with open('a3.txt', 'r') as f:
    text =  f.read().strip().replace('.', ' ')
    isCoveredMatrix = np.full_like(np.array([list(x) for x in text.split("\n")]), 0).astype('float64')

text = text.replace("\n", "")
symbolRegex = "[^\s\d\w]"
starRegex = "\*"
digitRegex = "\d+"

starDict = {}

allSymbolMatchIndices = [m.span() for m in re.finditer(symbolRegex, text)]
allDigitMatches = [(*m.span(), m.group(0)) for m in re.finditer(digitRegex, text)]
allStarMatches = [m.start(0) for m in re.finditer(starRegex, text)]

symbolCoverMatrix = np.ones((3,3))

def setIsCoveredMatrix(y, x):
    framedMatrix = np.zeros((isCoveredMatrix.shape[0]+2, isCoveredMatrix.shape[1]+2))
    framedMatrix[y:y+3,x:x+3] += symbolCoverMatrix
    return framedMatrix[1:isCoveredMatrix.shape[0]+1, 1:isCoveredMatrix.shape[1]+1]

def isCovered(matchTuple, matrix):
    y = int(matchTuple[0])//matrix.shape[0]
    x = int(matchTuple[0])%matrix.shape[1]
    xLen = matchTuple[1] - matchTuple[0]
    return np.sum(matrix[y, x:x+xLen]) > 0

for x in allSymbolMatchIndices:
    partilallyCoveredMatrix = setIsCoveredMatrix((int(x[0])//isCoveredMatrix.shape[0]), (int(x[0])%isCoveredMatrix.shape[0]))
    isCoveredMatrix += partilallyCoveredMatrix


sumOfAllCoveredDigits = np.sum([int(x[2]) for x in allDigitMatches if isCovered(x, isCoveredMatrix)])

print(sumOfAllCoveredDigits)

for m in allStarMatches:
    y = int(m)//isCoveredMatrix.shape[0]
    x = int(m)%isCoveredMatrix.shape[1]
    starDict[(y,x)] = []

for m in allDigitMatches:
    framedMatrix = np.zeros((isCoveredMatrix.shape[0]+2, isCoveredMatrix.shape[1]+2))

    kernel = np.ones((3,(m[1] - m[0])+2))
    startY = m[0]//isCoveredMatrix.shape[0]
    startX = m[0]%isCoveredMatrix.shape[1]
    framedMatrix[startY:startY+3, startX:startX+(m[1]-m[0])+2] = kernel

    for k in starDict.keys():
        if framedMatrix[k[0]+1, k[1]+1] == 1:
            starDict[k].append(int(m[2]))


sumOfGearRatios = np.sum([np.prod(v) for v in starDict.values() if len(v) == 2])
print(sumOfGearRatios)
