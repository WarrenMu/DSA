import numpy as np

twoArray=np.array([[11, 15, 18, 6],[10, 14, 11, 5],[12, 17, 12, 8],[15, 18, 14, 9]])
print(twoArray)
print("---------------------------------------------------")

def traverseToArray(array):
    for i in range(len(array)):
        for j in range(len(array[0])):
            print(array[i][j])
            
traverseToArray(twoArray) 