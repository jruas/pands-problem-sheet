#Program takes a positive floating-point number as input and outputs an approximation of its square root

#Author: Joana Ruas

import math                                                 #Importing maths module

def newton(x):                                              #[REF4]: Newton Method: https://stackoverflow.com/questions/55232484/newtons-method-for-approximating-square-roots
   tolerance = 0.000001
   estimate = 1.0
   while True:
        estimate = (estimate + x / estimate) / 2
        difference = abs(x - estimate ** 2)
        if difference <= tolerance:
            break
   return estimate

num=input('Please insert a posivite floating point: ')   #Program taks positive floating point as input
NewtonSQ=newton(float(num))                              #Converts the user's number to float and runs the function newton

print('The square root of {} is {}'. format(num, NewtonSQ))
