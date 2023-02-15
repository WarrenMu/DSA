import numpy as np

twoArray=np.array([[11, 15, 18, 6],[10, 14, 11, 5],[12, 17, 12, 8],[15, 18, 14, 9]])
print(twoArray)
print("---------------------------------------------------")

def accessElement(array, rowIndex, columnIndex):
    if rowIndex>=len(array) and columnIndex >=len(array[0]):
        print("Incorrect index")
    else:
        print(array[rowIndex][columnIndex])
        
accessElement(twoArray, 1, 2)