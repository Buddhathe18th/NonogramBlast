class Nonogram:
    size = 10  # Default size
    nums = [[]] * 2 * size # Default numbers are empty, columns first, then the row numbers
    board = [[0] * size] * size

    def __init__(self,size,nums=0,board=0):
        if not(type(size)==int and size>0):
            raise Exception("Size of board has to be a positive integer")
        self.size = size
        if nums==0 and board==0:
            # raise Exception("Empty board and numbers, please specify at least one")
            x=1
        elif nums!=0 and board!=0:
            self.checkValid() # TODO: write checkValid()
        elif nums!=0:
            self.nums=nums
        else:
            self.board=board

    def __str__(self):

        sideLength= self.renderSideNums()[0]


        topLength=0 # How many to shift down
        for i in range(0,self.size):
            temp=len(self.nums[i])-1
            for j in self.nums[i]:
                temp = temp + len(str(j))

            if topLength < temp:
                topLength = temp








        string="Size: "+str(self.size)+"\n\n"+"Nums: "+str(self.nums)+"\n\n"+"Board:\n\n" # Headers
        for row in self.board:
            string=string+('\t'.join(str(x) for x in row))+"\n" # Board itself
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

    def checkValid(self):
        return 0
