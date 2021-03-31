#This is a program that asks a user to input a string and outputs every second letter in reverse order.
#Author: Joana Ruas


string=input('Please insert a sentence')                                #Asking user to input a string

 
stringReverse=(string[::-1])                                            #Reversing order of string into another variable. [REF2]:https://www.w3schools.com/python/python_howto_reverse_string.asp)

#Output in reverse order, but missing every second string.              #[REF3]:#Source:https://stackoverflow.com/questions/57986268/remove-every-second-character-must-be-alphabetical-or-numerical-of-a-string-wi)


i = 1                                                                   # i needs to start in 1 instead of zero, so that the first letter to be ommited was T and not h, because of the %2 considiton.
s2 = ""
for char in stringReverse:
    if char.isalpha() or char.isnumeric() or char==" ":
        if (i % 2) == 0:
            s2 += char
        i += 1 
    else:
        s2 += char
stringReverse=s2

print (s2)