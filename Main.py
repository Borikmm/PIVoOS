import pygame
import sys
import time
import random
from pygame.color import THECOLORS

from Desktop import Desktop


pygame.init()

dysplay_width, dysplay_hight = pygame.display.Info().current_w, pygame.display.Info().current_h

if __name__ == "__main__":
    pygame.display.set_caption("Крутая игра")
    Desktop()