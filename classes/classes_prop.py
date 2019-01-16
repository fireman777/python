#!/usr/bin/env python36

#class without properties - myMoney is called like a method

class Pocket:
    def myMoney(self):
        print('$100')

a=Pocket()
a.myMoney()

#class with properties - function myMoney looks like a variable
class Pocket2:
    @property
    def myMoney(self):
        print('100$')

b=Pocket2()
b.myMoney
