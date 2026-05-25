import pygame as pg
from pygame.event import Event

WIDTH = 640
HEIGHT = 480
BG_COLOR = (20,50,50)

class MainMenu:
    def __init__(self):
        pg.display.set_caption('wizardshut - menu')
        self.buttons = []

    def draw(window: pg.surface):
        window.fill(BG_COLOR)