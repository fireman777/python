#!/usr/bin/env python36

#open file1.txt and copy each symbol to file3.txt

myfile = open("file1.txt", "r")
cont=myfile.read()

myfile3 = open("file3.txt", "w")
for i in cont:
    myfile3.write(i)

myfile.close()
myfile3.close()