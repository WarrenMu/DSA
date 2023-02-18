#clear() method
print('--------------------------------------------------')

myDict = {'name':'Edy','age':26}

myDict.clear()
print(myDict)
print('--------------------------------------------------')
dict = myDict.copy()
print(dict)
print('--------------------------------------------------')
#fromkeys()
newDict = {}.fromkeys([1,2,3],0)
print(newDict)
print('--------------------------------------------------')
print(myDict.get('boy',24))

print('--------------------------------------------------')
# items(), keys(), popitem(), setdefault(), pop(), update()