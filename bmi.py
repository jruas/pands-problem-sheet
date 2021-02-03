# This program is the answer to weekly Task 02
# Author: Joana Ruas

# The program calculates the Body Maxx Index (BMI)

height = float(input ('Please insert your height:'))
weight = float(input ('Please insert your weight:'))
newheight = (height/100)
bmi = (weight/newheight**2)


print ('BMI is '+ str(round(bmi,2))+".")