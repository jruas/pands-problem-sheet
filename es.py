# program starts asking the user to name a file to be created
#filename=input('Please insert the name for the file (example: hello.txt): ')

import sys

filename=sys.argv[1]                                                        #[REF]: https://www.tutorialspoint.com/How-to-read-a-file-from-command-line-using-Python


def readFile ():                                                            #Function to read file and count 'E' or 'e'
    count=0                                                                 #[REF]:https://www.geeksforgeeks.org/python-count-occurrences-of-a-character-in-string/
    with open(filename, "r") as f:
        for line in f:
            for i in line:
                if i =='e' or i=='E':
                    count=count+1
    print('The number of e is: {}'. format(count))      

readFile()