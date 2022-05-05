import pygame
from pygame.locals import *
import sys

pygame.init()

#version for testing
testing_on = True
skip_intro = False

#variables and objects
screen_width = 1000
screen_height = 800

screen = pygame.display.set_mode((screen_width, screen_height)) #areas in game will be 1000 x 760, the down stripe will be used for player status  

clock = pygame.time.Clock()

#changing title
pygame.display.set_caption("Megawarps")

#changing icon
icon = pygame.image.load("images/icon.png")
pygame.display.set_icon(icon)

#basic functions
def to_finish(event):
    if event.type == pygame.QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
        sys.exit()
        pygame.quit()
        return True
    return False
    
        
    
