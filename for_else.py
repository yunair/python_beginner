#!/usr/bin/python
#-*-coding:utf-8-*-
for x in range(5):
    print x
    if x == 1:
        continue
    if x == 2:
        pass #单纯的占位作用
    if x == 3:
        exit()
    if x == 4:
        break;
    print "#"
else:
    print "ending"

for x in range(5):
    print "-"*10,">",x
