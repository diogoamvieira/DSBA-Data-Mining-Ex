"""Given and integer number, use a loop to find its factorial"""

n = int(input('Choose a number: '))

fact = 1

for i in range(1,n+1):
    fact = fact * i

print('The factorial number of ', n, ' is:', fact)