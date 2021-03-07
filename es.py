# program starts asking the user to name a file to be created
filename=input('Please insert the name for the file (example: hello.txt): ')
usertext=input('Please insert the content for the file: ')

#creating the file with the name from input

def writeFile ():
    with open (filename, "wt") as f:
        f.write(usertext)

#function to create and write the file is called:
writeFile()

#read file and counting: 
# reference for counting:  https://www.geeksforgeeks.org/python-count-occurrences-of-a-character-in-string/
def readFile ():
    count=0
    with open(filename, "r") as f:
        for line in f:
            for i in line:
                if i =='e' or i=='E':
                    count=count+1
    print('The number of e is: {}'. format(count))      

readFile()