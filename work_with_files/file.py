#!/usr/bin/env python36

#open/close file using try/finally and push all content to variable
try:
    file1 = open("file1.txt")
    file1_content=file1.read()
finally:
    file1.close()

#read file line by line
file  = open("file1.txt")
for line in file:
    if line in ('\n', '\r\n'):
        print('<<< EMPTY line >>>')
    else:
        print(line, end='')
file.close()

#open/close file using with and write there from var
with open("file3.txt", "w") as file3:
    amount_written=file3.write(file1_content)
    print('written {} letters'.format(amount_written))
