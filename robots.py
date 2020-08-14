#!/usr/bin/env python36

class Robot:
    '''Представляет робота с именем.'''
    #Переменная класса, содержащая количество роботов
    population=0

    def __init__(self,name):
        '''Инициализация данных.'''
        self.name  name
        print('Инициализация {0}.'.format(self.name))
        '''Инициализация данных.'''

        Robot.population += 1

    def __del__(self):
        '''Я умираю.'''
        print('{} уничтожается!'.format(self.name))
        Robot.population -= 1
        if Robot.population == 0:
            print('{} был последним.'.format(self.name))
        else:
            print('Осталось {0:d} работающих роботов.'.format(Robot.population))
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
