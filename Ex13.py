'''Asks the user to write a sequence of words split by commas;
b.Prints that list sorted alphabetically. (Eg.: a,c,b -> [a,b,c])'''

user_list = input('Write a sequence of words split by commas: ')

user_list = user_list.split(', ')

user_list.sort()

print(user_list)