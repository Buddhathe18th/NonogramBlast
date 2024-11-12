import tools
import re

# boardTest=tools.Nonogram(2,[[1,1],[2],[0],[2]],[[True, False],[False, False]])
#
# arr=[['2', '13'], ['2', '2'], ['2'], ['2'], ['5', '2'], ['3', '1', '1', '1'], ['3', '1', '1', '1'], ['1', '5'], ['6'], ['1', '5'], ['8', '1'], ['7', '7'], ['7', '3'], ['1'], ['5'], ['3'], ['5'], ['1', '3'], ['2', '6'], ['2', '1', '2']]

# k=[]
# for i in arr:
#     t=[]
#     for j in i:
#         t.append(int(j))
#     k.append(t)

# bt=tools.Nonogram(10,k)
# print(bt)
# bt.solve()
# print(bt)
# print(bt.board)
# bt.solve()
# print(bt)
# # print(bt.checkSolved())
# print(bt.checkValid())
#
# print(boardTest)
# print(boardTest.renderRow(0))
#
# print(tools.Nonogram.findSolutions([6],""))

boardTest=tools.Nonogram(2,[[0],[2],[1],[1]])
# print(boardTest.renderRow(1))
# print(boardTest.allPosibilities(boardTest.renderRow(1)))
# print(boardTest.findSolutions([2],"  "))

print(boardTest.lineScore([1,1,1],"     "))
print(boardTest.lineScore([4],"     "))
print(boardTest.lineScore([4]," 111 "))
