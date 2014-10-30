#!/usr/bin/python

#str
s = "abcd"
#list
l = [1,2,3,'a','b']
#tuple
t = (7,8,9,'x','y')
#dict
d = {1:111, 2:222, 5:555, 6:666}

for x in s:
    print x

for y in l:
    if y >= 2:
        print y,
print

for z in t:
    print z,
print

for key in d:
    print key,
    print d[key]

for k,v in d.items():
    print k, v

#range(i,j,k) "i" start "j" end "k" step
#default i=0 k=1
for x in range(10):
    print x
for x in range(1,9):
    print x
for x in range(1, 10, 2):
    print x

string = "hello"
for x in range(len(string)):
    print string[x]
