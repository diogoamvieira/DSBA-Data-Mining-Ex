'''gives the volume of the cylinder and the surface area of that cylinder'''

import numpy as np

pi = np.pi

r = int(input('Choose a Radius for a Cylinder: '))
h = int(input('Choose a Height for a Cylinder: '))

totalvolume = pi * r ** 2 * h
surface = 2 * pi * r * 2 + 2 * pi * r * h

print('The cylinder has a volume of: ', totalvolume)
print('... and the surface is: ', surface)