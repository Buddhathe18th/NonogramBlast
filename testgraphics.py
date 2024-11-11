import pygame
import tools
from test import *
import Button
import Nums

pygame.init()

screen=pygame.display.set_mode((800,600))

location_x=200
location_y=200

# add all blocks to the background
def gameboardui(nonogram):
    y=0
    mygameboardbuttons=[]
    mygameboard=nonogram.board
    print(mygameboard)
    for i in mygameboard:
        for j in range(nonogram.size):

            mygameboardbuttons.append(Button.Button((j%nonogram.size)*30, y, i[j]))
            print(i[j])
            if (j+1)%nonogram.size == 0:
                y=y+30
    return mygameboardbuttons

pygame.font.init() # you have to call this at the start,
                   # if you want to use this module.
my_font = pygame.font.SysFont('Comic Sans MS', 15)





run = True
selectedbuttons = []
bt=tools.Nonogram(10,[[3,1,1,1],[2,4],[6],[4],[2,2],[1,2],[4],[5],[2,3],[2,5],[2,3],[2,1,1],[1,1,2],[1,2],[1,1],[5,1,1],[6,1,1],[3,3],[4,3],[1,3]])
mygameboardbuttons=gameboardui(bt)

background = pygame.Surface((30*bt.size,30*bt.size))

def drawTop(nonogram):
    x=[]
    for i in range(nonogram.size):
        for j in range(len(nonogram.nums[i])):
            number=Nums.Num(str(nonogram.nums[i][j]))
            number.draw(screen,30*i+location_x,location_y-(len(nonogram.nums[i])-j)*30)

while run:

    screen.fill((202, 228, 241))
    screen.blit(background,(location_x,location_y))
    num1.draw(screen,0,0)

    arrTop=[]
    for i in range(bt.size):
        for j in range(len(bt.nums[i])):
            Nums.Num(str(bt.nums[i][j])).draw(screen,30*i+location_x,location_y-(len(bt.nums[i])-j)*30)

    for i in range(bt.size):
        for j in range(len(bt.nums[i+bt.size])):
            Nums.Num(str(bt.nums[i+bt.size][j])).draw(screen,location_x-(len(bt.nums[i+bt.size])-j)*30,i*30+location_y)




    # event handler
    for event in pygame.event.get():
        # quit game
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()

    pygame.display.update()

