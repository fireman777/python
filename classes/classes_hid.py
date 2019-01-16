#!/usr/bin/env python36

#work with classes - hidden classes

class schoolMember:
    popul=0
    def __init__(self,name,age):
        self.name=name
        self._age=age
        schoolMember.popul+=1
        print('School has {0} members.'.format(schoolMember.popul))


#vasya=schoolMember('Vasya',45)
#print(vasya.name)
#print(vasya._age)

#petya=schoolMember('Petro',15)
#print(petya.name)
#print(petya._age)


