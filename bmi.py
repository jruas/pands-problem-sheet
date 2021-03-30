# This program is the answer to weekly Task 02
# Author: Joana Ruas

# The program calculates the Body Maxx Index (BMI)
# Program takes from user weight (kg) and height (cm)
# Outputs the BMI in weight by m2


height = float(input ('Please insert your height in centimetres:'))     #Conversion of input to Float, as input is a string by default.
weight = float(input ('Please insert your weight in Kilograms:'))


newheight = (height/100)                                                #Conversion of height to metres.  
bmi = round((weight/newheight**2),2)                                    #BMI calculation and conversion to 2 decimal places.

print('BMI is {}.' .format(bmi))                                        #Output of BMI