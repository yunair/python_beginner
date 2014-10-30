#!/usr/bin/python
#global var
x = 'I am a global var'

def fun():
    x = 100
    global y
    y = 200
    print x

def changeGlobalFun():
    global x
    x = 5
    print x

fun()
print 'x = ', x
print 'y = ', y

changeGlobalFun()
print 'x = ', x
print 'y = ', y




