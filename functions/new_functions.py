#!/usr/bin/env python3

def total(initial=5, *numbers, **keywords):
    count=initial
#    return numbers
#    for number in numbers:
#        count+=number
#    return count
    for key in keywords:
        count+=keywords[key]
    return keywords[key]
    
    for i in keywords:
      print (i)

print(total(10,1,2,3,vegatables=50,fruits=100))

