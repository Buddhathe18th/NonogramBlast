import re
class Nonogram:
    size = 10  # Default size
    nums = [[]] * 2 * size # Default numbers are empty, columns first, then the row numbers
    board = [[0] * size] * size # Sub array is each row, input as boolean array
    correct = 0 # If the nums is the known, change to 1, if board is known, change to 2, change to 3 if solved

    def __init__(self, size, arr1, arr2=None):
        if arr2==None:
            if not (type(size) == int and size > 0):
                raise Exception("Size of board has to be a positive integer")
            self.size = size
            self.nums = [[]] * 2 * size
            self.board = [[0] * size] * size

            if type(arr1[0][0]) == int:  # nums
                if not (len(arr1) == 2 * self.size):
                    raise Exception("Numbers are not the right dimensions.")
                self.nums = arr1
                self.correct = 1
            elif type(arr1[0][0]) == bool:  # board
                if not (len(arr1) == self.size):
                    raise Exception("Board is not the right dimensions.")
                self.board = arr1
                self.correct = 2
            else:
                raise Exception("Input array is not the right dimensions")

        else:
            if not(type(size)==int and size>0):
                raise Exception("Size of board has to be a positive integer")
            self.size = size
            self.nums = [[]] * 2 * size
            self.board = [[0] * size] * size

            self.correct=1 # Default

            if arr1!=0 and arr2!=0:
                check=True
                if not(len(arr1) == 2 * self.size and len(arr2) == self.size):
                    check=False
                for i in arr2:
                    if len(i)!=self.size:
                        check=False
                if not check:
                    raise Exception("Numbers and boards are not the right dimensions.")
                self.checkValid() # TODO: write checkValid()
                self.nums=arr1
                self.board=arr2

    def __str__(self):

        sideLength= self.renderSideNums()[0]
        sideNums= self.renderSideNums()[1]
        topLength= self.renderTopNums()[0]
        topNums= self.renderTopNums()[1]




        string="Size: "+str(self.size)+"\n\n"+"Nums: "+str(self.nums)+"\n\n"+"Board:\n\n" # Headers

        for i in range(topLength):
            temp=""
            temp = temp + " " * (sideLength+3)
            for j in range(self.size):
                temp=temp+topNums[j][i]+"\t"
            temp=temp+"\n"
            string=string+temp

        string=string+"\n"
        for i in range(self.size):
            string = string + sideNums[i] + "\t"
            for x in self.board[i]:
                if x==True:
                    string=string+"1\t"
                else:
                    string=string+"0\t"
            string=string+"\n"
        return string


    def renderSideNums(self):
        sideLength = 0  # How many to shift right
        for i in range(self.size, 2 * self.size):
            temp = len(self.nums[i]) - 1
            for j in self.nums[i]:
                temp = temp + len(str(j))

            if sideLength < temp:
                sideLength = temp

        sideBar=[""]*self.size
        for i in range(self.size):
            temp=""
            for j in self.nums[i+self.size]:
                temp=temp+str(j)+" "
            temp=temp[:-1]
            sideBar[i]=temp.rjust(sideLength)

        return [sideLength,sideBar]

    def renderTopNums(self):
        topLength=0 # How many to shift down
        for i in range(0,self.size):
            temp=len(self.nums[i])-1
            for j in self.nums[i]:
                temp = temp + len(str(j))

            if topLength < temp:
                topLength = temp

        topBar = [""] * self.size
        for i in range(self.size):
            temp = ""
            for j in self.nums[i]:
                temp = temp + str(j) + " "
            temp = temp[:-1]
            topBar[i] = temp.rjust(topLength)

        return [topLength,topBar]

    def renderRow(self,ind):
        row="".join(self.board[ind])
        return row


    def checkValid(self):
        for i in range(0,self.size):
            x=1

