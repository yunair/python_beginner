#!/usr/bin/python
#coding:utf8
#global var
a = 100
"""
default var for function
"""
def fun(x, y=1):
    if x == y:
        print x == y
    else:
        print x != y
x = raw_input("输入字符: ")
y = raw_input("input_something")
fun(x)
