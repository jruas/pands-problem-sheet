# pands-problem-sheet : JOANA RUAS
----------------------------------


# Week 1:
- Setting up environment
- Installing git hub
- Linking pands-problem-sheet to git hub

# Week2: 
#### Calculation of Body Mass Index (BMI), getting weight and height from user.

#### file: bmi.py

##### Key-sections of code:
- [x] Take in height and weight from user
- [x] Conversion of input values to float
- [x] Conversion of height to metres
- [x] BMI calculation
- [x] Printing result to user with 2 decimal places in a string "BMI is XX.XX"

# Week 3:
#### Taking a string. Output every second letter in reserve order

#### file: secondstring.py

##### Key-sections of code:
- [x] Take in string from user.
- [x] Reverse that string. [REF2]
- [x] Loop to run the string and only outputs every second letter. [REF3]
- [x] Loop starting in i=1 and not i=0 to start in second letter and not first.

# Week 4:
#### Program asks user to input an integer. Outputs successive values of the following calculation: At each step, calculates the next value by taking the current value. If it is even, divide by two, if it is odd, multiply it by three.

#### file: collatz.py

##### Key-sections of code:
- [x] Take positive integer from user.
- [x] Verify if input is positive integer. If not, ask again.
- [x] Create an empty list.
- [x] Append the user's number to the list created.
- [x] If statement for the two situations (number is even or number is odd)

# Week 5:
#### Program outputs whether or not today is a weekday.

#### file: weekday.py

##### Key-sections of code:
- [x] Importing Python datetime module
- [x] Getting todays date from datetime function. [REF4]
- [x] Converting date into weekday index, using weekday function from datetime. [REF5]
- [x] Creating a tuple of Strings of Weekdays (with indexes corresponding to weekday function indexes) 
- [x] If statement: if today's index less than five, so it is weekday.

# Week 6:
#### Program takes a positive floating-point number as input and outputs an approximation of its square root

#### file: squareroot.py

##### Key-sections of code:
- [x] Importing maths module.
- [x] Taking floating point number from user as input.
- [x] Converting to float
- [x] Defining netwon function. [REF6]
- [x] Reunning newton function with number from user.

# Week 7:



# Week 8:
#### Program displays a plot of the functions f(x)=x, g(x)=x2 and h(x)=x3, in the range [0,4]

#### file: plottask.py

##### Key-sections of code:
- [x] Importing matplotlib.pyplot.
- [x] Importing Numpy.
- [x] Generate array from 0 to 4 with numpy.
- [x] Generate functions f(x), g(x) and h(x) from x.
- [x] Define plot (function to represent, colours, labels).
- [x] Save plot into png figure.




# References
- [REF1]: General formating of README file (https://docs.github.com/en/github/writing-on-github/basic-writing-and-formatting-syntax) 
- [REF2]: Reversing a string (secondstring.py) (://www.w3schools.com/python/python_howto_reverse_string.asp)
- [REF3]: Loop for missing every second string (secondstring.py) (https://stackoverflow.com/questions/57986268/remove-every-second-character-must-be-alphabetical-or-numerical-of-a-string-wi)
- [REF4]: Getting today's date (weekday.py) (https://stackoverflow.com/questions/32490629/getting-todays-date-in-yyyy-mm-dd-in-python)
- [REF5]: Weekday() function (weekday.py) (https://docs.python.org/3/library/datetime.html)
- [REF6]: Newton Method (squareroot.py) https://stackoverflow.com/questions/55232484/newtons-method-for-approximating-square-roots