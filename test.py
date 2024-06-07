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

print(tools.Nonogram.findSolutions([1,1],"01 1"))
