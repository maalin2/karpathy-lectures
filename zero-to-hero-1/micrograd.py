'''
following along with zero to hero 1 - building micrograd
11/23/2023
'''

import math
import numpy as np
import matplotlib.pyplot as plt



def f(x):
    return 3*x**2 - 4*x + 5
    

f(3.0)

xs = np.arange(-5,5,0.25)
xs
 
ys=f(xs)
ys
 
 
plt.plot(xs,ys)