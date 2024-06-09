import pygame


# button class
class Button():
    # x,y are the top left corner coordinates, state is the state of the square, 1 for coloured, 0 for no colour, -1 for empty
    def __init__(self, x, y, state):
        width = 30
        height = 30
        self.rect = pygame.Rect(x, y, width, height)
        self.state = state
        self.clicked=False

    def draw(self, surface,surface_x,surface_y):
        action = False
        # get mouse position
        pos = pygame.mouse.get_pos()
        x, y = pos
        x = x- surface_x
        y=y - surface_y

        if self.state=="1":
            pygame.draw.rect(surface, (0, 0, 0), self.rect, 0)
        elif self.state=="0":
            pygame.draw.rect(surface, (255, 255, 255), self.rect, 0)
        else:
            pygame.draw.rect(surface, (100, 100, 100), self.rect, 0)

        for i in range(4):
            pygame.draw.rect(surface, (0, 0, 0), (self.rect.x - i, self.rect.y - i, 30, 30), 1)

        # check mouseover and clicked conditions
        if self.rect.collidepoint(x,y):
            if (pygame.mouse.get_pressed()[0] == 1) and self.clicked == False:
                self.clicked = True
                if self.state!="1":
                    self.state="1"
                else:
                    self.state=" "
            if (pygame.mouse.get_pressed()[2] == 1) and self.clicked == False:
                self.clicked = True
                if self.state != "0":
                    self.state = "0"
                else:
                    self.state = " "

            if pygame.mouse.get_pressed()[0] == 0 and pygame.mouse.get_pressed()[2] == 0:
                self.clicked = False

            # surface.blit(self.rect, (self.rect.x, self.rect.y))

            return action
