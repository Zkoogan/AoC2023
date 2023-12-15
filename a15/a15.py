import numpy as np

with open('a15.txt', 'r') as f:
    data = list(map(lambda v: list(v), f.read().split(",")))

hashMap = {}
boxKeys = np.arange(256)

for box in boxKeys:
    hashMap[box] = []

def calcHash(sequence):
    hash = 0
    for c in sequence:
        hash = ((hash + ord(c))*17) % 256
    return hash

def removeFromBox(key):
    hash = calcHash(key)
    return (hash, [x for x in hashMap[hash] if key != x[0]])

def addToBox(key, value):
    hash = calcHash(key)
    temp = hashMap[hash]
    for lens in hashMap[hash]:
        if lens[0] == key:
            lens[1] = value
            return (hash, temp)
    
    temp.append([key,value])
    return (hash, temp)

print(np.sum([calcHash(x) for x in data]))

for x in data:
    hash, boxValues = removeFromBox(''.join(x[:-1])) if x[-1] == '-' else removeFromBox(''.join(x[:-1]))
    hashMap[hash] = boxValues

products = []

for hash in hashMap.keys():
    for k, v in enumerate(hashMap[hash]):
        print(k, v, hash)
        products.append((hash + 1)*(k+1)*int(v[1]))

print(np.sum(products))