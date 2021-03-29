# This program is the answer to weekly Task 02
# Author: Joana Ruas

# The program calculates the Body Maxx Index (BMI)
# Program takes from user weight (kg) and height (cm)
# Outputs the BMI in weight by m2


height = float(input ('Please insert your height in centimetres:'))     #Converstion of input to Float, as input is a string by default.
weight = float(input ('Please insert your weight in Kilograms:'))


newheight = (height/100)                                                #Converstion of height to metres.  
bmi = (weight/newheight**2)                                             #bmi calculation


print ('BMI is '+ str(round(bmi,2))+".")