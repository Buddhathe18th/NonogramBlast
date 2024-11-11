import pygame
import Solver.tools as tools
from Solver.test import *
import Button
import Nums


pygame.init()

screen=pygame.display.set_mode((800,600))


# add all blocks to the background
def makeButtons(nonogram):
    y=0
    mygameboardbuttons=[]
    mygameboard=nonogram.board
    print(mygameboard)
    for i in mygameboard:
        for j in range(nonogram.size):

            mygameboardbuttons.append(Button.Button((j%nonogram.size)*30, y, i[j]))
            if (j+1)%nonogram.size == 0:
                y=y+30
    return mygameboardbuttons

def renderNumbers(nonogram,location_x,location_y):
    for i in range(bt.size):
        for j in range(len(bt.nums[i])):
            Nums.Num(str(bt.nums[i][j])).draw(screen,30*i+location_x,location_y-(len(bt.nums[i])-j)*30)

    for i in range(bt.size):
        for j in range(len(bt.nums[i+bt.size])):
            Nums.Num(str(bt.nums[i+bt.size][j])).draw(screen,location_x-(len(bt.nums[i+bt.size])-j)*30,i*30+location_y)

run = True
bt=Solver.tools.Nonogram(10,[[3,122,1,1],[2,4],[6],[4],[2,2],[1,2],[4],[5],[2,3],[2,5],[2,3],[2,1,1],[1,1,2],[1,2],[1,1],[5,1,1],[6,1,1],[3,3],[4,3],[1,3]],[[' ', '1', ' ', ' ', '0', '0', '0', '0', '0', ' '], ['1', '0', '0', '1', ' ', ' ', ' ', '0', ' ', ' '], ['0', '1', '0', '1', ' ', ' ', '0', '1', '1', '1'], [' ', '0', ' ', ' ', '1', ' ', ' ', ' ', '1', '0'], ['0', ' ', '0', '0', '0', ' ', ' ', '0', '0', ' '], ['0', '1', '0', ' ', '1', '1', ' ', '0', '0', ' '], [' ', '1', '1', '0', '1', ' ', ' ', ' ', ' ', '1'], ['0', '1', ' ', ' ', '1', '1', '1', ' ', ' ', ' '], [' ', ' ', ' ', '0', ' ', '0', '0', '1', '1', '0'], [' ', '0', '1', ' ', ' ', '0', '1', '0', '1', '1']])
mygameboardbuttons=makeButtons(bt)

background = pygame.Surface((30*bt.size,30*bt.size))

location_x=200
location_y=200

while run:
    screen.fill((202, 228, 241))
    screen.blit(background,(location_x,location_y))
    for i in mygameboardbuttons:
        i.draw(background,location_x,location_y)

    for i in range(bt.size):
        for j in range(len(bt.nums[i])):
            Nums.Num(str(bt.nums[i][j])).draw(screen, 30 * i + location_x, location_y - (len(bt.nums[i]) - j) * 30)

    for i in range(bt.size):
        for j in range(len(bt.nums[i + bt.size])):
            Nums.Num(str(bt.nums[i + bt.size][j])).draw(screen, location_x - (len(bt.nums[i + bt.size]) - j) * 30,i * 30 + location_y)

    # event handler
    for event in pygame.event.get():
        # quit game
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()