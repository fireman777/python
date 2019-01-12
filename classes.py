#!/usr/bin/env python3

#work with classes

class Animals():
        def __init__(self,name,color):
            self.name=name
            self.color=color

class Cats(Animals):
    def voice(self):
        print('meouu')

class Dogs(Animals):
    def voice(self):
        print('gav-gav')

tom=Cats('Tomas','green')
tom.voice
