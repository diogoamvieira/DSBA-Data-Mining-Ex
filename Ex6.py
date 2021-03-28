'''a.reads a file(txt file) containing more than 10 rows;
b.creates a new file which excludes the 10th row of the original one.'''

#reads a file(txt file)containing more than 10rows;
f = open('ex6file.txt', 'r')

lines = f.readlines()

f.close()

#creates a new file which excludes the 10th row of the original one.
del lines[9]

newfile = open('ex6newfile.txt', 'w+')

for line in lines:
    newfile.write(line)

newfile.close()

################################################
###   Not working well! It deletes 2 rows!   ###
################################################