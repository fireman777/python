#!/usr/bin/env python36

#open and close file using try/finally and push all content to variable
try:
    f = open("file1.txt")
    content=f.read()
finally:
    f.close()

#open file3.txt and pull there all the symbols from myfile1.txt
myfile3 = open("file3.txt", "w")
for i in content:
    amount_written=myfile3.write(i)

#add some bytes (symbols) and print their number
print(myfile3.write('abcdef'))
myfile3.close()

#print some bytes(symbols) of and close it using with statement
with open("file1.txt") as f:
        print(f.read())

