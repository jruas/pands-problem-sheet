#Newtown Method. Source: https://stackoverflow.com/questions/55232484/newtons-method-for-approximating-square-roots
import math

def newton(x):
   tolerance = 0.000001
   estimate = 1.0
   while True:
        estimate = (estimate + x / estimate) / 2
        difference = abs(x - estimate ** 2)
        if difference <= tolerance:
            break
   return estimate


#program takes in a positive floating point:
num=input('Please insert a posivite floating point: ')
#converting to float
NewtonSQ=newton(float(num))
#printing
print('The square root of {} is {}'. format(num, NewtonSQ))
