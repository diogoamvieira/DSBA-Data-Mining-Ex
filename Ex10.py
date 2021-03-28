"""Considerarray [[1,2,3],[4,5,6],[7,8,9]], delete its second column 
and insert  [[99,99,99]] on its place"""

import numpy as np

arr = np.array([[1, 2, 3],[4, 5, 6],[7, 8, 9]])

arr = np.delete(arr, 1, 1)

print(arr)

new_col = np.array([[99,99,99]])

new_arr = np.insert(arr, 1, new_col, axis=1)

print(new_arr)