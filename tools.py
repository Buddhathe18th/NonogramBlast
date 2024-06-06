class Nonogram:
    size = 10  # Default size
    nums = [[]] * 2 * size # Default numbers are empty, columns first, then the row numbers
    board = [[0] * size] * size

    def __init__(self,size,nums=0,board=0):
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

        string="Size: "+str(self.size)+"\n\n"+"Nums: "+str(self.nums)+"\n\n"+"Board:\n\n"
        for row in self.board:
            string=string+('\t'.join(str(x) for x in row))+"\n"
        return(string)


        # for i in nums[]


    def checkValid(self):
        return 0
