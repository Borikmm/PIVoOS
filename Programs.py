import pygame

class programs:
    pass




class window:
    width = None
    height = None
    x = None
    y = None

    border = None

    color = None
    screen = None


    def __init__(self, width, height, x, y, border, color, screen, com):
        self.width = width
        self.height = height
        self.x = x
        self.y = y

        self.border = border

        self.color = color
        self.screen = screen
        self.com = com

    def otr(self):
        pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.width, self.height), self.border)

    def check_tap(self, pos_cursor):
        if self.x < pos_cursor[0] < (self.x + self.width) and self.y < pos_cursor[1] < self.y + self.height:
            self.com()



    

