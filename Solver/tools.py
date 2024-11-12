import re
class Nonogram:
    size = 10  # Default size
    nums = [[]] * 2 * size # Default numbers are empty, columns first, then the row numbers
    board = [[" "] * size] * size # Sub array is each row, input as string
    correct = 0 # If the nums is the known, change to 1, if board is known, change to 2, change to 3 if solved


    # Technically 3 constructors, size must be included, showing the size of the board
    # The three different possibilities is to include the numbers, the board, or both


    def __init__(self, size, arr1, arr2=None):
        if arr2==None:
            if not (type(size) == int and size > 0):
                raise Exception("Size of board has to be a positive integer")
            self.size = size
            self.nums=[]
            for i in range(2*size):
                self.nums.append([])
            self.board=[]
            for i in range(size):
                t = []
                for j in range(size):
                    t.append(" ")

                self.board.append(t)

            if type(arr1[0][0]) == int:  # nums
                if not (len(arr1) == 2 * self.size):
                    raise Exception("Numbers are not the right dimensions.")
                self.nums = arr1
                self.correct = 1
            elif type(arr1[0][0]) == str:  # board
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
            self.nums = []
            for i in range(2 * size):
                self.nums.append([])
            self.board = []
            for i in range(size):
                t = []
                for j in range(size):
                    t.append(" ")

                self.board.append(t)

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
            temp = temp + " " * (sideLength+3)+"\t"
            for j in range(self.size):
                temp=temp+topNums[j][i]+"\t"
            temp=temp+"\n"
            string=string+temp

        string=string+"\n"
        for i in range(self.size):
            string = string + sideNums[i] + "\t\t"
            for x in self.board[i]:
                if x=="1":
                    string=string+"1\t"
                elif x=="0":
                    string=string+"0\t"
                else:
                    string=string+" \t"
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
        row=""
        for i in range(self.size):
            row=row+str(self.board[ind][i])
        return row

    def renderCol(self,ind):
        col=""
        for i in range(self.size):
            col = col + str(self.board[i][ind])
        return col

    def checkValid(self):
        check=True
        # Check rows
        for i in range(self.size):
            regex="^0*"
            for j in self.nums[i+self.size]:
                regex=regex+"1{"+str(j)+"}0+"
            regex=regex[:-1]+"*$"
            row=self.renderRow(i)

            if not re.match(regex,row):
                check=False

        # Check columns
        for i in range(self.size):
            regex="^0*"
            for j in self.nums[i]:
                regex=regex+"1{"+str(j)+"}0+"
            regex=regex[:-1]+"*$"
            col=self.renderCol(i)

            if not re.match(regex,col):
                check=False
        return check
    @staticmethod
    def allPosibilities(row, s=[]):
        strings = s

        spaces = row.count(" ")
        if spaces == 0:
            return strings

        if spaces == 1:
            temp = row
            strings.append(temp.replace(" ", "1"))
            temp = row
            strings.append(temp.replace(" ", "0"))
            return strings

        temp = row
        temp = temp.replace(" ", "1", 1)
        Nonogram.allPosibilities(temp, strings)

        temp = row
        temp = temp.replace(" ", "0", 1)
        Nonogram.allPosibilities(temp, strings)
        return strings


    @staticmethod
    def findSolutions(nums,row): # Input rows as 0,1 and spaces, num is the given pattern
        solutions=Nonogram.allPosibilities(row)

        sol=row

        regex = "^0*"
        for i in nums:
            regex = regex + "(1){" + str(i) + "}0+"
        regex=regex[:-1]+"*$"

        i=0
        while i<len(solutions):
            if re.match(regex,solutions[i])==None:
                solutions.remove(solutions[i])
                i=i-1
            i=i+1

        # Check for guaranteed 1s
        for i in range(len(row)):
            bool=1
            for k in solutions:
                bool=bool and int(k[i])
            if bool==1:
                bool=True
            else:
                bool=False
            if bool and row[i]==" ":
                sol=sol[0:i]+"1"+sol[i+1:]

        # Check for guaranteed 0s
        for i in range(len(row)):
            bool = 1
            for k in solutions:
                bool = bool and not int(k[i])
            if bool == 1:
                bool = True
            else:
                bool = False
            if bool and row[i] == " ":
                sol = sol[0:i] + "0" + sol[i + 1:]
        return sol

    # Define a function where the score of a line is calculated
    # A line with a higher score in theory should have most valid moves at this time.

    def lineScore(self, nums,line):
        
        score=0

        sum=0
        for i in nums:
            sum=sum+i
        score=sum/len(nums)-1

        consecutiveSpaces=len(re.findall("( )+",line))
        spaces=len(re.findall(" ",line))
        return score+consecutiveSpaces-spaces

    def solve(self):
        while (not self.checkSolved()):
            # Solving all the columns
            for i in range(self.size):
                colNums=self.nums[i]
                col=self.renderCol(i)

                col=Nonogram.findSolutions(colNums,col)

                for j in range(self.size):
                    self.board[j][i]=col[j]

            for i in range(self.size):
                rowNums=self.nums[i+self.size]
                row=self.renderRow(i)

                row=Nonogram.findSolutions(rowNums,row)

                for j in range(self.size):
                    self.board[i][j]=row[j]

            print(self)

    def checkSolved(self):
        if any(' ' in sublist for sublist in self.board):
            return False

        if not self.checkValid():
            return False

        return True
