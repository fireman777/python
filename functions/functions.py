#!/usr/bin/env python3

#function with parameters
def func1(x,y):
    if x>0 and y>0:
        print ('ALL positive!')
    elif x<0 and y<0:
        print('All negativ')
    else:
        print('positiv/negativ')

#function with parameters with defaut value
def func2(message, number=5):
    '''Печатает сообщение указанное число раз.

    Если число не указано, то печатается 5 раз'''
    print(message*number)

#func2('Hello')
#func2("Hi, my name is Slim Shady. ",4)
#func2('Кукареку ',2

#function with key parameters
def func3(one=1,two=2,three=3,four=4,five=5):
    '''Функция с ключевыми параметрами.

    Можно задать любой параметр в любом месте.'''
  print(one,two,three,four,five)


func3(four=44,one=11)

