myList=[1,2,3,4,5,6,7]
print(myList)
myList[2]=33
print(myList)
print("-------------------------------------")

myList2=[1,2,3,4,5,6,7,8,9,0]
print(myList2)
myList2.insert(0,11)
print(myList2)
print("-------------------------------------")

myList2.append(0.5)
print(myList2)
print("-------------------------------------")

myList2.extend(myList)
print(myList2)