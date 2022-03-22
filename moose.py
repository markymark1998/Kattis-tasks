#! /usr/bin/python3
import sys

for line in sys.stdin:
    lr = line.split()
    l = int(lr[0])
    r = int(lr[1])
    even = True

    if l == r:
        if l == 0 and r == 0:
            print("Not a moose")
        else:
            print("Even ", end='')
            print(l+r)
    elif l < r:
        print("Odd ", end='')
        print(r * 2)
    elif r < l:
        print("Odd ", end='')
        print(l * 2)
