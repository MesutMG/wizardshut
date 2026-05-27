import pygame as pg
from util.button import Button
from scene import Scene

class MainMenu(Scene):
    def __init__(self):
        super().__init__("menu")
        self.buttons = []
        self.button1 = Button(20, 20, 100, 50, "helo", onePress=True)

    def draw(self, window, mousePos, mouseStatus):
        l = self.button1.process(mousePos, mouseStatus)
        window.blit(l[0], l[1])