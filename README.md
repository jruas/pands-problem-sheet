# GMIT 2021
# Programming and Scripting
# Weekly Tasks
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
- [x] Taking in height and weight from user
- [x] Converting input values to float
- [x] Converting height to metres
- [x] BMI calculation
- [x] Printing result to user, with 2 decimal places as "BMI is XX.XX"

# Week 3:
#### Taking a string. Output every second letter in reserve order

#### file: secondstring.py

##### Key-sections of code:
- [x] Taking in a string from user.
- [x] Reversing that string. [REF2]
- [x] Loop to run the string and only outputs every second letter. [REF3]
- [x] Loop starting in i=1 and not i=0 to start in second letter and not first.

# Week 4:
#### Program asks user to input an integer. Outputs successive values of the following calculation: At each step, calculates the next value by taking the current value. If it is even, divide by two, if it is odd, multiply it by three.

#### file: collatz.py

##### Key-sections of code:
- [x] Taking a positive integer from user.
- [x] Verifying if input is positive integer. If not, ask again.
- [x] Creating an empty list.
- [x] Appendding the user's number to the list created.
- [x] If statement for both situations (even or odd number)

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
#### Program reads in a text tile and outputs the number of e's it contains.
#### Program to take the filname from an argument on the command line

#### file: es.py

##### Key-sections of code:
- [x] Importing sys module (to be able to read document from command line).
- [x] Defining variable filename as sys.argv[1] to be able to read from command line. [REF7]
- [x] Defining function to read file.
- [x] Counting 'e' and 'E' in the text tile. [REF8]
- [x] Print count


# Week 8:
#### Program displays a plot of the functions f(x)=x, g(x)=x2 and h(x)=x3, in the range [0,4]

#### file: plottask.py

##### Key-sections of code:
- [x] Importing matplotlib.pyplot.
- [x] Importing Numpy.
- [x] Generating array from 0 to 4 with numpy.
- [x] Generating functions f(x), g(x) and h(x) from x.
- [x] Defining plot (function to represent, colours, labels).
- [x] Saving plot into png figure.




# References
- [REF1]: General formating of README file (https://docs.github.com/en/github/writing-on-github/basic-writing-and-formatting-syntax) 
- [REF2]: Reversing a string (secondstring.py) (://www.w3schools.com/python/python_howto_reverse_string.asp)
- [REF3]: Loop for missing every second string (secondstring.py) (https://stackoverflow.com/questions/57986268/remove-every-second-character-must-be-alphabetical-or-numerical-of-a-string-wi)
- [REF4]: Getting today's date (weekday.py) (https://stackoverflow.com/questions/32490629/getting-todays-date-in-yyyy-mm-dd-in-python)
- [REF5]: Weekday() function (weekday.py) (https://docs.python.org/3/library/datetime.html)
- [REF6]: Newton Method (squareroot.py) (https://stackoverflow.com/questions/55232484/newtons-method-for-approximating-square-roots)
- [REF7]: Read file from command line (es.py) (https://www.tutorialspoint.com/How-to-read-a-file-from-command-line-using-Python)
- [REF8]: Read file from command line (es.py) (https://www.geeksforgeeks.org/python-count-occurrences-of-a-character-in-string/)