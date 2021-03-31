#Program outputs wether today is a weekday or not
#Reference: https://pythontic.com/datetime/date/weekday
#Author: Joana Ruas

import datetime                                                                         #importing Python datetime module

today=datetime.date.today()                                                            #Getting todays date from datetime function. [REF]: https://stackoverflow.com/questions/32490629/getting-todays-date-in-yyyy-mm-dd-in-python 
weekday=today.weekday()                                                                #Converting date into weekday, where weekday is represented by a number. [REF]: https://docs.python.org/3/library/datetime.html


weekDays=('Moday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday') #Creating a tuple of Strings of Weekdays, where the indice corresponds to the same indexes of function weekday

if weekday < 5:
    todayString=weekDays[weekday]                                                      #Variable for today, where assigns the number from weekday() to the acctual weekday from tuple 
    print('Unfortunatly today is {}, weekday' . format(todayString))
else:
    ('Today is weekend!')


