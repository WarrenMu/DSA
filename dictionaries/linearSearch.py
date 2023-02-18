myDict = {'name':'Edy','age':26}

def search(dict, value):
    for key in dict:
        if dict[key]==value:
            return key,value
    return 'The value does not exist'

print(search(myDict,26))


#del pop() popitem() amortized O(n) time complexity