from math import *
import numpy as np
# read sample files

def open_file(file_name,DATA_PATH = "" ):
    """ Function to open file and return data in nested lists"""
    with open(DATA_PATH + file_name) as file1:
        
        lines1 = file1.readlines()
        m = len(file1.readlines()) #number of rows
        n = len(maxlines1[0].split(',')) # columns

        data1 = np.array(

            #loop through rows

            [float(n.strip()) for n in line.split(',')]     #loop through columns 
        )


        data1 = []
        for line in lines1:
            row = []
            for n in line.split(','):
                row.append(float(n.strip()))
            data1.append(row)
        return data1

with open('data2.csv') as file2:
    lines2 = file2.readlines()
    data2 = []
    for line in lines2:
        row = []
        for n in line.split(','):
            row.append(float(n.strip()))
        data2.append(row)

with open('weights.csv') as filew:
    linew = filew.read()
    w = []
    for n in linew.split(','):
        w.append(float(n.strip()))

results = []
for i in range(len(data1)):
    s = 0
    for j in range(len(w)):
        d = data1[i][j] - data2[i][j]
        s += w[j] * abs(d)
    results.append(s)

critical = 0
for i in range(len(results)):  # for all i
    if results[i] > 5:
        critical = critical + 1  # increase by 1
if critical == 1:
    print("criticality: 1 result above 5")
else:
    print("criticality:", critical, "results above 5")
