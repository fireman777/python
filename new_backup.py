#!/usr/bin/env python3

def show_choice():
        print('Choose:\t1. Copy\n\t2. Zip\n\t3. Exit.')

def copy():
    print('Copy done.')

def zip():
    print('zip done.')



def wrong_choice():
    print('<<',c,'>> is not a correct answer!')

show_choice()
while True:
    c=input('what is your choice?')
    try:
        c=int(c)
    except ValueError:
        print('Not a string!')
    if c==1:
        copy()
        break
    elif c==2:
        zip()
        break
    elif c==3:
        print('Good Bye!')
        break
    else:
        wrong_choice()

