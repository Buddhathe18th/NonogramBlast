import pygame


# button class
class Num():
    # x,y are the top left corner coordinates, state is the state of the square, 1 for coloured, 0 for no colour, -1 for empty
    def __init__(self, value):
        width = 30
        height = 30
        self.value = value
        self.clicked=False

    def draw(self, surface,surface_x,surface_y):
        textFace=pygame.Surface((30,30),pygame.SRCALPHA, 32)
        pygame.font.init()

        my_font = pygame.font.SysFont('Comic Sans MS', 15)
        t = my_font.render(self.value, False, (0, 0, 0))
        text_rect = t.get_rect(center=(30 / 2, 30 / 2))
        textFace.blit(t,text_rect)

        surface.blit(textFace,(surface_x,surface_y))
