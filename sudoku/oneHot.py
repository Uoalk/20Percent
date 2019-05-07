import numpy as np
def toOneHot(arr):
    out = []
    for i in range(9):
        row = []
        for j in range(9):
            temp = [0, 0, 0, 0, 0, 0, 0, 0, 0]
            if int(arr[i*9+j]) != 0:
                temp[int(arr[i*9+j])-1] = 1
            row.append(temp)
        out.append(row)
    return out

a = []
file = open("puzzle.csv", "r") 
for x in range(2):
    a.append(toOneHot(file.readline()[:-1].replace(" ", "").split(',')))
np.save("oneHot", a)
file.close()