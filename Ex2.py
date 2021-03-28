'''print only the characters present at an even index number'''

string = input('Write something: ')

for count, value in enumerate(string):
    if (count % 2) == 0:
        print(value)