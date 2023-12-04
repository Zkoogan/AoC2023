import numpy as np
import re
import math

with open('a4.txt', 'r') as f:
    data =  [x.split(':')[1].replace('\n', '').strip() for x in f.readlines()]

data = [(x.split('|')[0].strip(), x.split('|')[1].strip()) for x in data]
data = [(re.split('\s+', x[0]), re.split('\s+', x[1])) for x in data]

data = [list(set(x[0]) & set(x[1])) for x in data]

score = int(np.sum([math.pow(2, len(x))//2 for x in data]))

print(score)

numScratchCards = np.ones(len(data))

for index, matches in enumerate(data):
    numScratchCards[index+1:index+len(matches)+1] += numScratchCards[index]

print(int(np.sum(numScratchCards)))