import pygame
import tools
from test import *
import Button

pygame.init()

screen=pygame.display.set_mode((800,600))


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

run = True
selectedbuttons = []
bt=tools.Nonogram(10,[[' ', '1', ' ', ' ', '0', '0', '0', '0', '0', ' '], ['1', '0', '0', '1', ' ', ' ', ' ', '0', ' ', ' '], ['0', '1', '0', '1', ' ', ' ', '0', '1', '1', '1'], [' ', '0', ' ', ' ', '1', ' ', ' ', ' ', '1', '0'], ['0', ' ', '0', '0', '0', ' ', ' ', '0', '0', ' '], ['0', '1', '0', ' ', '1', '1', ' ', '0', '0', ' '], [' ', '1', '1', '0', '1', ' ', ' ', ' ', ' ', '1'], ['0', '1', ' ', ' ', '1', '1', '1', ' ', ' ', ' '], [' ', ' ', ' ', '0', ' ', '0', '0', '1', '1', '0'], [' ', '0', '1', ' ', ' ', '0', '1', '0', '1', '1']])
mygameboardbuttons=gameboardui(bt)

background = pygame.Surface((30*bt.size,30*bt.size))

location_x=100
location_y=100
while run:

    screen.fill((202, 228, 241))
    screen.blit(background,(location_x,location_y))
    print(pygame.mouse.get_pressed())



    for i in mygameboardbuttons:
        i.draw(background,location_x,location_y)

    # for x in range(bt.size*bt.size):
    #     if mygameboardbuttons[x].draw(screen):
    #
    #         print(mygameboardbuttons[x].getNumber())
    #         mygameboardbuttons[x].image = pygame.transform.scale(greenpicture(mygameboardbuttons[x].getNumber()),
    #                                                              (int(300 * 0.1), int(300 * 0.1)))
    #         selectedbuttons.append(x)
    #         print("length of slected buttons is " + str(len(selectedbuttons)))
    #         if len(selectedbuttons) == 2:
    #             if selectedbuttons[0] == selectedbuttons[1]:
    #                 mygameboardbuttons[selectedbuttons[0]].image = pygame.transform.scale(
    #                     bluepicture(mygameboardbuttons[selectedbuttons[0]].getNumber()),
    #                     (int(300 * 0.1), int(300 * 0.1)))
    #             else:
    #                 if checknumber(selectedbuttons[0], selectedbuttons[1], mygameboard):
    #                     mygameboardbuttons[selectedbuttons[0]].image = pygame.transform.scale(blue0, (
    #                     int(300 * 0.1), int(300 * 0.1)))
    #                     mygameboardbuttons[selectedbuttons[0]].setNumber(0)
    #                     mygameboard[selectedbuttons[0]] = 0
    #                     mygameboardbuttons[selectedbuttons[1]].image = pygame.transform.scale(blue0, (
    #                     int(300 * 0.1), int(300 * 0.1)))
    #                     mygameboardbuttons[selectedbuttons[1]].setNumber(0)
    #                     mygameboard[selectedbuttons[1]] = 0
    #                     mygameboard = deletelines(mygameboard, cleangameboard(mygameboard))
    #                     mygameboard = deletelines(mygameboard, cleangameboard(mygameboard))
    #                     refreshpage(mygameboardbuttons, mygameboard)
    #
    #                 else:
    #                     mygameboardbuttons[selectedbuttons[0]].image = pygame.transform.scale(
    #                         bluepicture(mygameboardbuttons[selectedbuttons[0]].getNumber()),
    #                         (int(300 * 0.1), int(300 * 0.1)))
    #                     mygameboardbuttons[selectedbuttons[1]].image = pygame.transform.scale(
    #                         bluepicture(mygameboardbuttons[selectedbuttons[1]].getNumber()),
    #                         (int(300 * 0.1), int(300 * 0.1)))
    #             selectedbuttons = []
    #     # mygameboardbuttons[x].setNumber(0)
    #
    # if hintbutton.draw(screen):
    #     hintnumbers = hintcheck(mygameboard)
    #     print(hintnumbers)

    # event handler
    for event in pygame.event.get():
        # quit game
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()