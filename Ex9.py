"""Sum arrays [[1, 2, 3], [10,10, 10]] and [[4, 2, 3], [1,1, 10]]
and, then, create a new array containing the square of each element."""

import numpy as np

array1 = np.array([[1, 2, 3], [10, 10, 10]])
array2 = np.array([[4, 2, 3], [1, 1, 10]])

sumarrays = array1 + array2

squared_values = []

for i in np.nditer(sumarrays):
    i = i ** 2
    squared_values.append(i)

np_squared_values = np.array(squared_values)

print(np_squared_values)