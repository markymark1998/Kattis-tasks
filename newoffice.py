#! /usr/bin/python3

import sys
#import numpy as np (I do not think numpy can be used in Kattis)

officeX = 0
officeY = 0
officeArea = [] #
emp = 0
requests = []


counter = 0
for line in sys.stdin:
    split = line.split()
    length = len(split)
    if length == 0:
        break
    if length == 2:
        #Office area, everything should be reinitialized
        officeX = int(split[0])
        officeY = int(split[1])
        requests = []
        counter = 0
        #officeArea= [ ["unallocated"]*officeY]*officeX
        officeArea=[]
        for i in range(officeX):
            row = []
            for j in range(officeY):
                column = "unallocated"
                row.append(column)
            officeArea.append(row)

        #print(len(officeArea[0]))  #Y axis
        #print(len(officeArea))     #X axis

    elif length == 1:
        #Nr of employees
        emp = int(split[0])
    elif length == 5:
        #Employee. (Alice 2 3 10 11) for example.
        name = split[0]
        requests.append(name)
        x = int(split[1])
        y = int(split[2])
        x2 = int(split[3])
        y2 = int(split[4])

        for i in range(x, x2):
            for j in range(y, y2):
                '''if officeArea[i][j] != 'unallocated':
                    #if officeArea[i][j] != name:
                    officeArea[i][j] = 'contested'
                elif officeArea[i][j] == 'unallocated':
                    officeArea[i][j] = str(name) #name occupies the space'''
                if officeArea[i][j] == "unallocated":
                    officeArea[i][j] = name
                else:
                    officeArea[i][j] = 'contested'
        counter = counter + 1

        if counter == emp:
            tempDict = {}
            '''for x in range(officeX):
                for y in range(officeY):
                    if officeArea[x][y] in tempDict:
                        currDict = {officeArea[x][y]: tempDict[officeArea[x][y]] + 1}
                        tempDict.update(currDict)

                    else:
                        defString = str("{'" + officeArea[x][y] + "':" + "1}")
                        currDict = eval((defString))
                        tempDict.update(currDict)
            '''
            for column in officeArea:
                for space in column:
                    if space in tempDict:
                        currDict = {space: tempDict[space] + 1}
                        tempDict.update(currDict)
                    else:
                        #defString = str("{'" + space + "':" + "1}")
                        #currDict = eval((defString))
                        currDict = {space: 1}
                        tempDict.update(currDict)
            print("Total ", end='')
            print(officeX * officeY)
            print("Unallocated ", end='')
            if "unallocated" in tempDict:
                print(tempDict["unallocated"])
            else:
                print(0)
            print("Contested ", end=' ')
            if "contested" in tempDict:
                print(tempDict["contested"])
            else:
                print(0)



            for name in requests:
                print(name, end=' ')
                if name in tempDict:
                    print(tempDict[name])
                else:
                    print(0)

