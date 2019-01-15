#!/usr/bin/env python36

#open file1.txt and push all test to variable
myfile1 = open("file1.txt", "r")
content = myfile1.read()
myfile1.close()

#open file3.txt and pull there all the symbols from myfile1.txt
myfile3 = open("file3.txt", "w")
for i in content:
    amount_written=myfile3.write(i)

#add some bytes (symbols) and print their number
print(myfile3.write('abcdef'))
myfile3.close()

#print some bytes(symbols) of file1.txt and close it using try and finally
try:
    f = open("file1.txt")
    print(f.read(19))
finally:
    f.close()

#print some bytes(symbols) of and close it using with statement
with open("file1.txt") as f:
        print(f.read())

