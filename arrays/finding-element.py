from array import *

arr=array('b', [1,2,3,4,5,6])

def find(array,value):
    for i in array:
        if i == value:
            return array.index(value)
    return "Element doesnt exist"

print(find(arr, 5))