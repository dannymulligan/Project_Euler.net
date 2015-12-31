#!/usr/bin/python

def triangle(n):
    t = 0
    for i in xrange(1,n+1):
        t += i
        yield t


i = 0
for x in triangle(n = 16):
    i += 1
    print("Triangle number {} = {}".format(i, x))
