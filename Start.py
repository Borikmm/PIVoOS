import pygame
import sys
import time
import random
from pygame.color import THECOLORS


pygame.init()
n = "?"
a = 0
b = 0
width = 500
height = 500
cube_size = 20
skok_cube = ((width*height)//cube_size**2)
ckok_uge = 0
po_y = height/cube_size
po_x = width/cube_size

screen = pygame.display.set_mode((width, height))

# Text Antialias = сглаживание
screen.fill(THECOLORS['white'])
font = pygame.font.SysFont('couriernew', cube_size-10)
#font = pygame.font.SysFont('couriernew', cube_size)
#text = font.render(str(f'{n}'), True, THECOLORS['green'])
#screen.blit(text, (50, 50))

def apr(cube_size):
    global a, b, width, height, skok_cube, ckok_uge, po_y, po_x, n, font
    while ckok_uge <= skok_cube:
        r = pygame.Rect(a, b, cube_size, cube_size)
        pygame.draw.rect(screen, (255, 0, 0), r, 1)
        text = font.render(str(f'{n}'), True, THECOLORS['black'])
        screen.blit(text, (a, b))

        if po_x == 0:
            if po_y == 0:
                pass
            else:
                a = 0
                po_x = width/cube_size
                po_y -= 1
                b += cube_size
        else:
            po_y = height/cube_size
            po_x -= 1
            a += cube_size
            ckok_uge += 1
  #          n += 1
        pygame.display.flip()
        print("otr")

apr(cube_size)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            color = (255, 255, 255)
    pygame.display.flip()