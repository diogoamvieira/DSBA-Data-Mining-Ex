'''Check if a string contains a ‘x’ followed by one or more ‘y’'''
string = 'geoxyc'

string = [*string]

for i in string:
    if i != 'y':
        continue
    elif i == 'y' and string[-1] == 'x':
        print('string contains a ‘x’ followed by one or more ‘y’')
    else:
        print('string doesnt contain an ‘y’ after ‘x’')


###################################
###   Not working!! Hmmmmmmmm   ###
###################################