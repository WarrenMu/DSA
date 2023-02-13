from array import *
#Creating an array and traverse.
my_array=array('i',[1,2,3,4,5])

for i in my_array:
    print(i)
    
#Access individual elements through indexes.
print("--------------------------------- ")
print(my_array[0])

#Append any value to the array using append() method
print("--------------------------------- ")
print("Step 3")
my_array.append(6)
print(my_array)
#Insert value in an array using insert() method
print("--------------------------------- ")
my_array.insert(1,4)
print(my_array)
#Extend python array using extend() method
print("--------------------------------- ")
my_arr=array('i',[7,8,9,10])
my_array.extend(my_arr)
print(my_array)
#Add items from list into array fromlist() method
print("--------------------------------- ")
tempList=[11,12,13,14,15]
my_array.fromlist(tempList)
print(my_array)
#Remove any array element using remove() method
print("--------------------------------- ")
my_array.remove(15)
print(my_array)
#Remove last array element using pop() method
print("--------------------------------- ")
my_array.pop(14)
print(my_array)
#Fetch any element through its index using index() method
print("--------------------------------- ")
print(my_array.index(4))
#Reverse python array using reverse() method
print("--------------------------------- ")
my_array.reverse()
print(my_array)