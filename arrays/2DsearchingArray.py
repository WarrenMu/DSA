import numpy as np

twoArray=np.array([[11, 15, 18, 6],[10, 14, 11, 5],[12, 17, 12, 8],[15, 18, 14, 9]])
print(twoArray)
print("---------------------------------------------------")

def searchToArray(array, value):
    for i in range(len(array)):
        for j in range(len(array[0])):
            if array[i][j] == value:
                return 'The value is located at index ' + str(i)+"  "+str(j)
           
            
print(searchToArray(twoArray,14))