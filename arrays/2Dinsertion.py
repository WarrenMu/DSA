import numpy as np

twoArray=np.array([[11, 15, 18, 6],[10, 14, 11, 5],[12, 17, 12, 8],[15, 18, 14, 9]])
print(twoArray)
print("---------------------------------------------------")
newTwoArray= np.insert(twoArray, 0 ,[[1,2,3,4]], axis=0 )#axis=0 is for row while axis=1 is for column
print(newTwoArray)
print("---------------------------------------------------")
newTwoArray= np.append(twoArray, [[11,22,33,44]], axis=0)
print(newTwoArray)