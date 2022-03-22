#! /usr/bin/python3
import sys

alternate = True # This will correspond to #, false means .
first = True
pixels = 0
pixelsSum = 0
errorEncoding = False
chars = ["#","."]
n = 0
nCounter = 0
counter = 0
printer = ""
for line in sys.stdin:
    l = line.split()

    if len(l) == 1:
        #New image, check if previous worked.

        counter = 0
        n = int(line)
        pixels = 0
        pixelsSum = 0
        if n == 0:
            break

        if first:
            first = False
        else:
            print()
    else:
        alternator = False
        if l.pop(0) == "#":
            alternator = True
        pixels = 0
        for i in l:
            if alternator:
                print('#'*int(i), end='')
                alternator = False
            else:
                print('.' * int(i), end='')
                alternator = True
            pixels = pixels + int(i)

        if pixelsSum != 0:
            if pixelsSum != pixels:
                errorEncoding = True
        pixelsSum = pixels
        #counter = counter + 1
        '''if pixelsSum == 0:
            pixelsSum = pixels
        else:
            if pixelsSum != pixels:
                errorEncoding = True
            pixelsSum = pixels
        '''
        print()
        counter = counter + 1
        if counter == n:
            if errorEncoding:
                print("Error decoding image")
                errorEncoding = False


