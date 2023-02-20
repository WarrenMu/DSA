newTurple1= tuple('abcdef')

# print('b' in newTurple1)

def search(turp, element):
    for i in turp:
        if i == element:
            print('\nThe element is: ')
            return turp.index(i)
    return 'The element does not exist'

print(search(newTurple1, 'e'))