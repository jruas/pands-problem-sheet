#Program asks usee to input a positive integer
#Outputs the following calculation:
#in each step,the next value by taking the current value, and if, it is even, divide it by two, but it is is off, multiply it by three and add one.
#program ends if current value is one.

#Author: Joana Ruas


number=int(input('Please insert a positive integer: '))

if number <=0:
    print('Wrong!')
    number=int(input('Please try again: '))

numberslist=[]
numberslist.append(int(number))

while number !=1:
    if number %2==0:
        number=number/2
        numberslist.append(int(number))
    else:
        number=(number*3)+1
        numberslist.append(int(number))

print(numberslist)

