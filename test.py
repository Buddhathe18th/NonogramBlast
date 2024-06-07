import tools
import re

# boardTest=tools.Nonogram(2,[[1,1],[2],[0],[2]],[[True, False],[False, False]])
#
# bt=tools.Nonogram(2,[[2],[0],[1,0],[1,0]],[[True, False],[True, False]])
# print(bt)
# print(bt.checkValid())
#
# print(boardTest)
# print(boardTest.renderRow(0))


def allPosibilities(row, s=[]):
    strings = s

    spaces = row.count(" ")
    if spaces == 0:
        return strings

    if spaces==1:
        temp=row
        strings.append(temp.replace(" ", "1"))
        temp = row
        strings.append(temp.replace(" ", "0"))
        return strings

    temp = row
    temp=temp.replace(" ", "1",1)
    allPosibilities(temp,strings)

    temp = row
    temp=temp.replace(" ", "0",1)
    allPosibilities(temp, strings)
    return strings

print(allPosibilities("   "))
