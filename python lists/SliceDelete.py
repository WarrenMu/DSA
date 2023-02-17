myList=['a','b','c','d','e','f']
print(myList)
print("-------------------------------------")

print(myList[-1::-1])
print("-------------------------------------")

myList[0:2]=['x','y']
print(myList[:])
print("-------------------------------------")

# we can delete using
#   -pop() //deletes the last element without a given value
#   -remove()
#   -del

myList.pop()
print(myList)
print("-------------------------------------")
myList.pop(4)
print(myList)
print("-------------------------------------")

del myList[2]
print(myList)
print("-------------------------------------")

myList.remove('x')
print(myList)
print("-------------------------------------")







