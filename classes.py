#!/usr/bin/env python3

#version 2.0-make .zip archieve of repo

class numb:
    def __init__(self,number_1,number_2):
      self.number_1=number_1
      self.number_2=number_2
    
    def mnoz(self,number_1,number_2):
        print(number_1*number_2)
        
    def delen(self,number_1,number_2):
        print(number_1/number_2)

    def plus(self,number_1,number_2):
        print(number_1+number_2)
    
    def minus(self,number_1,number_2):
        print(number_1-number_2)

numbers=numb(5,6)
numbers.plus()

#from code
