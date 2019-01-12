#!/usr/bin/env python3

#work with classes

class Animals():
        def __init__(self,name,color):
            self.name=name
            self.color=color
        def voice(self):
            print('Animals don\'t speak!')

class Cats(Animals):
    def voice(self):
        print('meouu')

class Dogs(Animals):
    def voice(self):
        print('gav-gav')
    def supervoice(self):
        super().voice()

dingo=Dogs('Dingo','black')
dingo.voice()
dingo.supervoice()
print(dingo.name,dingo.color)

#Dogs(1,2).voice()
#Dogs(1,2).supervoice()



