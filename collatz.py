#Program asks user to input a positive integer
#Outputs the following calculation:
#in each step,the next value by taking the current value, and if, it is even, divide it by two, but it is is off, multiply it by three and add one.
#program ends if current value is one.

#Author: Joana Ruas


number=int(input('Please insert a positive integer: '))                         #Taking positive integer from user

if number <=0:                                                                  #Verifying if input is a positve integer.
    print('Wrong!')                                     
    number=int(input('Please try again: '))                                     #If not, asking user again

numberslist=[]                                                                  #Creating an empty list
numberslist.append(int(number))                                                 #Appending input number to that list

while number !=1:                                                               #While number is not 1 the program is running 
    if number %2==0:                                                            #If number is even
        number=number/2
        numberslist.append(int(number))
    else:                                                                       #If number is odd
        number=(number*3)+1
        numberslist.append(int(number))

print(numberslist)                                                              #printing output

