import numpy as np

with open('a13.txt', 'r') as f:
    data = f.read().split("\n\n")

leftSideColumns = 0
upperRows = 0

savedValues = {}

for dataSetIndex, dataSet in enumerate(data):
    dataSet = np.array(list(map(lambda v: list(v), dataSet.split("\n"))))
    maxY, maxX = dataSet.shape
    savedX = 0
    savedY = 0
    for rowIndex, row in enumerate(dataSet):
        if rowIndex > 0:
            reflectionIndex = rowIndex-1
            if np.all(row == dataSet[rowIndex - 1, :]):
                matching = True
                counter = 1
                while matching and reflectionIndex - counter >= 0 and maxY > rowIndex + counter:
                    matching = True if np.all(dataSet[rowIndex+counter, :] == dataSet[reflectionIndex - counter, :]) else False
                    counter += 1
                if matching:
                    upperRows += rowIndex
                    savedY = rowIndex
                

    dataSetTransp = dataSet.transpose()
    for colIndex, col in enumerate(dataSetTransp):
        if colIndex > 0:
            reflectionIndex = colIndex-1
            if np.all(col == dataSetTransp[colIndex - 1, :]):
                matching = True
                counter = 1
                while matching and reflectionIndex - counter >= 0 and maxX > colIndex + counter:
                    matching = True if np.all(dataSetTransp[colIndex+counter, :] == dataSetTransp[reflectionIndex - counter, :]) else False
                    counter += 1
                if matching:
                    leftSideColumns += colIndex
                    savedX = colIndex
    savedValues[dataSetIndex] = (savedY, savedX)
                
print(savedValues)
    
print(np.sum([leftSideColumns, 100*upperRows]))

leftSideColumns = 0
upperRows = 0

for dataSetIndex, dataSet2 in enumerate(data):
    formattedDataSet = np.array(list(map(lambda v: list(v), dataSet2.split("\n"))))
    maxY, maxX = formattedDataSet.shape
    savedRow = 0
    savedColumn = 0
    for i in range(maxY):
        for j in range(maxX):      
            dataSet = np.array(formattedDataSet)
            dataSet[i, j] = '.' if dataSet[i,j] == '#' else '#'
            for rowIndex, row in enumerate(dataSet):
                if rowIndex > 0:
                    reflectionIndex = rowIndex-1
                    if np.all(row == dataSet[rowIndex - 1, :]):
                        matching = True
                        counter = 1

                        while matching and reflectionIndex - counter >= 0 and maxY > rowIndex + counter:
                            matching = True if np.all(dataSet[rowIndex+counter, :] == dataSet[reflectionIndex - counter, :]) else False
                            counter += 1

                        if matching and savedValues[dataSetIndex][0] != rowIndex:
                            savedRow = rowIndex

            dataSetTransp = dataSet.transpose()
            for colIndex, col in enumerate(dataSetTransp):
                if colIndex > 0:
                    reflectionIndex = colIndex-1
                    if np.all(col == dataSetTransp[colIndex - 1, :]):
                        matching = True
                        counter = 1

                        while matching and reflectionIndex - counter >= 0 and maxX > colIndex + counter:
                            matching = True if np.all(dataSetTransp[colIndex+counter, :] == dataSetTransp[reflectionIndex - counter, :]) else False
                            counter += 1

                        if matching and savedValues[dataSetIndex][1] != colIndex:
                            savedColumn = colIndex

    upperRows += savedRow
    leftSideColumns += savedColumn
                
    
print(np.sum([leftSideColumns, 100*upperRows]))