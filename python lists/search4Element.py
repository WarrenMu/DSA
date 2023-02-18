myList=[10,20,30,40,50,60,70,80,90]

# if 20 in myList:
#     print(myList.index(20))
# else:
#     print("Value does not exist")

#linear search

def searchList(list, value):
    for i in list:
        if i == value:
            return list.index(value)
    return 'The value does not exist in the list'
        
print(searchList(myList,80))