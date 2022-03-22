#! /usr/bin/python3

import sys

definitions = {}
alternator = True #True refers to a variable, False refers to an operation (such as +).
#operations = []
value = {}
for line in sys.stdin:
    split = line.split()
    if split[0] == "clear":
        definitions = {}
    elif split[0] == "def":
        defString = str("{'" + split[1] + "':" + split[2] + "}")
        currDict = eval(defString)
        definitions.update(currDict)
    else:
        unknown = False
        previousValue = 0
        operations = []

        for item in split:
            if item == "calc":
                print(end='')

            elif alternator:
                print(item, end=' ')
                alternator = False
                if item in definitions:
                    print(end='')
                    if len(operations) == 0:
                        previousValue = definitions[item]
                    elif operations[0] == "+":
                        previousValue = previousValue + definitions[item]
                    elif operations[0] == "-":
                        previousValue = previousValue - definitions[item]
                else:
                    unknown = True

            elif not alternator:
                print(item, end=' ')
                if len(operations) == 0:
                    operations.append(item)
                else:
                    operations[0] = item
                alternator = True
        if unknown:
            print("unknown")
        else:
            found = False
            for key in definitions:
                if definitions[key] == previousValue:
                    print(key)
                    found = True
            if not found:
                print("unknown")