from array import *

arr=array('b', [1,2,3,4,5,6])

def access(array,index):
    if index >= len(array):
        print("Theres no element in the list")
    else:
        print(array[index])
        
access(arr,3)