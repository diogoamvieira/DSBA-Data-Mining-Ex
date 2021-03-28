'''Create a list of float numbers: 
    a.ask the user for thelist size;
    b.ask the user foreach of the elements, individually;
    c.return the list.'''

userlist = []
x = 0

size = int(input('Choose a list size: '))

while len(userlist) < size:
    x = int(input('Choose a number for the list: '))
    userlist.append(x)
    
    
print('Your final list!', userlist)