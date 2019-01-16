#!/usr/bin/env python36

#work with classes - inheritance

class Animals():
        def __init__(self,name,color):
            self.name=name
            self.color=color
            print('Hi, my name is {0}'.format(self.name))
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


