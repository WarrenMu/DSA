import numpy as np

twoArray=np.array([[11, 15, 18, 6],[10, 14, 11, 5],[12, 17, 12, 8],[15, 18, 14, 9]])
print(twoArray)
print("---------------------------------------------------")

newToArray=np.delete(twoArray, 0, axis=0)
print(newToArray)