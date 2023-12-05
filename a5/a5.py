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

def calculateSeedToSoil(seeds):
    return findMapping("seed-to-soil map", seeds)

def calculateSoilToFertilizer(soils):
    return findMapping("soil-to-fertilizer map", soils)

def calculateFertilizerToWater(fertilizers):
    return findMapping("fertilizer-to-water map", fertilizers)

def calculateWaterToLight(waters):
    return findMapping("water-to-light map", waters)

def calculateLightToTemperature(lights):
    return findMapping("light-to-temperature map", lights)

def calculateTemperatureToHumidity(temperatures):
    return findMapping("temperature-to-humidity map", temperatures)

def calculateHumidityToLocation(humidities):
    return findMapping("humidity-to-location map", humidities)

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


a = calculateHumidityToLocation(calculateTemperatureToHumidity(calculateLightToTemperature(calculateWaterToLight(calculateFertilizerToWater(calculateSoilToFertilizer(calculateSeedToSoil(dataDict["seeds"])))))))

min = 92034785452836478952346789523456796234567895 #ridiculously large number

for i in range(0,len(dataDict["seeds"]),2):
    start, length = dataDict['seeds'][i:i+2]
    start = int(start)
    length = int(length)
    end = start + length
    moreNumbers = True
    step = 100000

    while(moreNumbers):
        if(end < start + step):
            step = end - start
            moreNumbers = False
        seeds = np.arange(start, start+step)
        minOfBatch = np.min(calculateHumidityToLocation(calculateTemperatureToHumidity(calculateLightToTemperature(calculateWaterToLight(calculateFertilizerToWater(calculateSoilToFertilizer(calculateSeedToSoil(seeds))))))))
        min = np.min([min,  minOfBatch])


print(np.min(a), min)
