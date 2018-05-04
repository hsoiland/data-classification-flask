#Import Packages
import csv
from sklearn import preprocessing
import numpy as np

# This function takes a column of the raw matrix and finds unique values for encoding
def uniqueItems(column):
    list = np.unique(column)
    fixedList = []
    for item in list:
        fixeListItem = [item]
        fixedList.append(fixeListItem)
    return fixedList

def newWidth(column):
    return len(np.unique(column))

def encodeColumn(oldCol, encoder):
    newCol = []
    for c in oldCol:
        newCol.append(encoder.transform(c).toarray())
    return np.array(newCol)

# Binarize the column with trueVal becoming +1 and everything else -1
def binarizeColumn(oldCol, trueVal):
    return [1 if x==trueVal else -1 for x in oldCol]

# Read the raw data file into arrays
with open('german.data.txt') as rawDataFile:
    csvReader = csv.reader(rawDataFile, delimiter=' ', quotechar='|')
    rows = []
    for row in csvReader:
        cols = []
        for col in row:
            # Change the value here into a floating point number
            if col[0] == 'A':
                value = float(col[1:])
            else:
                value = float(col)
            cols.append(value)
        rows.append(cols)

rowCount = len(rows)
colCount = len(rows[0])

# read it into an ndarray
newData = np.array(rows)

from sklearn.preprocessing import LabelEncoder
lblenc_1 = LabelEncoder()
lblenc_1.fit_transform(newData([]))
