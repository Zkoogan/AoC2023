import numpy as np
import re
from time import perf_counter

regex = '\d{1}'

numDict = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}

with open('a1.txt', 'r') as f:
    Lines = np.array(f.readlines())

def sum(calibrationValues):
    return np.sum(np.array(calibrationValues).astype('uint32'))

def firstDigit(calibValue):
    return re.search(regex, calibValue).group(0)

def lastDigit(calibValue):
    return re.search(regex, calibValue[::-1]).group(0)

def substituteTextForDigits(lines):
    curatedInput = list()
    for x in lines:
        fixedString = x
        a = re.search('(one|two|three|four|five|six|seven|eight|nine)', x)
        if(a):
            fixedString = fixedString[:a.span(0)[1]] + numDict[a.group(0)] + fixedString[a.span(0)[1]:]
        curatedInput.append(fixedString)
    return curatedInput

def substituteTextForDigitsBackwards(lines):
    curatedInput = list()
    for x in lines:
        fixedString = x[::-1]
        a = re.search('(eno|owt|eerht|ruof|evif|xis|neves|thgie|enin)', fixedString)
        if(a):
            fixedString = fixedString[:a.span(0)[0]] + numDict[a.group(0)[::-1]] + fixedString[a.span(0)[0]:]
        curatedInput.append(fixedString[::-1])

    return curatedInput

def substituteText(Lines):
    return zip(substituteTextForDigits(Lines), substituteTextForDigitsBackwards(Lines))

start = perf_counter()
print(sum([''.join([firstDigit(x), lastDigit(y)]) for x, y in substituteText(Lines)]))
print(perf_counter - start)