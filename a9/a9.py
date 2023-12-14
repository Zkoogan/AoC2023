import numpy as np

with open('a9.txt', 'r') as f:
    data =   np.array(list(map(str.split, f.readlines()))).astype('int64')

def calculateNextValueInSequence(sequence):
    if np.all(sequence == 0):
        return 0
    new_sequence = np.array([sequence[i + 1] - sequence[i] for i in range(len(sequence) - 1)])
    return sequence[-1] + calculateNextValueInSequence(new_sequence)

sums2 = [calculateNextValueInSequence(sequence[::-1]) for sequence in data]
sums1 = [calculateNextValueInSequence(sequence) for sequence in data]
print(np.sum(sums1), np.sum(sums2))