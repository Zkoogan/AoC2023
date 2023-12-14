import numpy as np

with open('a14.txt', 'r') as f:
    data = np.array(list(map(lambda v: list(v), f.read().split("\n"))))
    data2 = np.array(data)

states = {}

def genericTumbling(ioData):
    temp = ioData
    for rowIndex, row in enumerate(temp):
        for colIndex, col in enumerate(temp):
            if temp[rowIndex, colIndex] == 'O':
                currentDistance = rowIndex - 1
                if currentDistance >= 0:
                    continueTumblingUp = True
                    while continueTumblingUp and currentDistance >= 0:
                        if temp[currentDistance, colIndex] == '.':
                            temp[currentDistance, colIndex] = 'O'
                            temp[currentDistance+1, colIndex] = '.'
                            currentDistance -= 1
                        else:
                            continueTumblingUp = False

    return temp

print(np.sum(np.argwhere(genericTumbling(data)[::-1] == 'O')[:, 0]+1))

numTumblings = 1000000000
counter = 0
noCycle = True

while noCycle:
    counter += 1
    data2 = genericTumbling(data2)
    data2 = genericTumbling(data2.transpose()).transpose()
    data2 = genericTumbling(data2[::-1])[::-1]
    data2 = genericTumbling(data2.transpose()[::-1])[::-1].transpose()
    if states.get(np.array2string(data2), False):
        noCycle = False
    else:
        states[np.array2string(data2)] = counter

tumblesToFinish = (numTumblings - states.get(np.array2string(data2))) % (counter - states.get(np.array2string(data2))) + states.get(np.array2string(data2))

for i in range(tumblesToFinish):
    data2 = genericTumbling(data2)
    data2 = genericTumbling(data2.transpose()).transpose()
    data2 = genericTumbling(data2[::-1])[::-1]
    data2 = genericTumbling(data2.transpose()[::-1])[::-1].transpose()

print(np.sum(np.argwhere(data2[::-1] == 'O')[:, 0]+1))