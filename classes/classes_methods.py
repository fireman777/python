#!/usr/bin/env python36

#Instance, Class, and Static Methods
class MyClass:
    def method(self):
        return 'instance method called', self

    @classmethod
    def classmethod(cls):
        return 'class method called', cls

    @staticmethod
    def staticmethod():
        return 'static method called'

#obj=MyClass()
#print(obj.method())
print(MyClass.method(obj))
