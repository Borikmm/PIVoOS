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


    def __init__(self, width, height, x, y, border, color, screen, command):
        self.width = width
        self.height = height
        self.x = x
        self.y = y

        self.border = border

        self.color = color
        self.screen = screen
        self.command = command

    def otr(self):
        pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.width, self.height), self.border)

    def check_tap(self, pos_cursor):
        if self.x < pos_cursor[0] < (self.x + self.width) and self.y < pos_cursor[1] < self.y + self.height:
            self.command()



class Panel:

    window = None
    DRAW = False

    def __init__(self, width, height, x, y, border, color, screen):
        self.width = width
        self.height = height
        self.x = x
        self.y = y

        self.border = border

        self.color = color
        self.screen = screen


    def otr(self):
        if self.DRAW:
            pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.width, self.height), self.border)
            for i in self.window:
                i.otr()

    def check_tap(self, pos_cursor):
        for i in self.window:
            i.check_tap(pos_cursor)

    def change(self, per: bool):
        self.DRAW = per




    

