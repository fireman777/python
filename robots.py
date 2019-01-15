#!/usr/bin/env python36

class Robot:
    '''Представляет робота с именем.'''
    population=0

    def __init__(self, name):
        self.name=name
        print()
        print('Инициализация {0}.'.format(self.name))
        Robot.population+=1

    def sayhi(self):
        print('Привет, меня зовут {0}.'.format(self.name))

    def howmany():
        print('у нас {0:d} роботов.'.format(Robot.population))
    howmany=staticmethod(howmany)

droid1=Robot('Vasya')
droid1.sayhi()
Robot.howmany()

droid2=Robot('Petya')
droid2.sayhi()
Robot.howmany()

droid3=Robot('Grisha')
droid3.sayhi()
Robot.howmany()


