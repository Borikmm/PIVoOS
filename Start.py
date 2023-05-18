import random
import pygame
WIDTH, HEIGHT = 320, 240
pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
# use the first available font
font = pygame.font.SysFont(pygame.font.get_fonts()[0], 60)
pygame.display.set_caption("Centering Font Rect")

text = "maner"
widget = font.render(text, True, pygame.Color("seagreen"))
border = pygame.Rect(10, 10, WIDTH - 40, HEIGHT - 40)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            # change the text
            text = random.choice(["Short", "Long Looooong", ".", "+++", "ABC"])
            widget = font.render(text, True, pygame.Color("purple"))
        elif event.type == pygame.MOUSEWHEEL:
            # enlarge or shrink the border rect
            border.inflate_ip(event.y, event.y)
    screen.fill(pygame.Color("turquoise"))
    # draw border rect
    pygame.draw.rect(screen, pygame.Color("red"), border, width=1)
    # get the current font rect
    font_rect = widget.get_rect()
    # move rect to be centered on border rect
    font_rect.center = border.center
    screen.blit(widget, font_rect)
    # update display
    pygame.display.update()
pygame.quit()
