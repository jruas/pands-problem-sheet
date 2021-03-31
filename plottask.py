#Program that displays a plot of the functions:
# f(x)=x
# g(x)=x**2
# h(x)=x**3
# in the range [0,4] 
# Author: Joana Ruas
 

import matplotlib.pyplot as plt 
import numpy as np

xpoints=np.array(range(0,5))
fx=(xpoints)
gx=(xpoints**2) #Reference to exercise 3 from lab
hx=(xpoints**3)

plt.plot(xpoints,fx, color='red', label='f(x)')
plt.plot(xpoints,gx, color='blue', label='g(x)')
plt.plot(xpoints,hx, color='green', label='h(x)')

plt.title('Functions')      # Reference to exercise 10 from lab
plt.xlabel('X')             # Reference to exercise 10 from lab
plt.ylabel('Function of X') # Reference to exercise 10 from lab
plt.legend()                # Reference to exercise 10 from lab

plt.savefig('plotImage.png')
