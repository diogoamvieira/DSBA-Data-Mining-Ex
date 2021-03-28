'''Using  numpylibrary,  create  an  array with  valuesfrom  100  to 1000 
with  step=50, having 6 rows and 3 columns.'''

import numpy as np

values = [*range(100, 1000, 50)]

array = np.array(values).reshape(6, 3)

print(array)