import pygame
import sys
import time
import random
from pygame.color import THECOLORS

from Desktop import Desktop
from Start import loading_screen

pygame.init()

dysplay_width, dysplay_hight = pygame.display.Info().current_w, pygame.display.Info().current_h

if __name__ == "__main__":
    pygame.display.set_caption("Крутая игра")
    # loading_screen.run_loading()
    # pygame.quit()
    Desktop()