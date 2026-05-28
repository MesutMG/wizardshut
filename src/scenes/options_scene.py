import pygame as pg
from util.button import Button
from scenes.scene import Scene

class OptionsScene(Scene):
    def __init__(self, width: int, height: int, game):
        super().__init__("wizardshut - options", width, height, game)
        self.buttons = []
        self.button1 = Button(50, 50, 200, 70, "back to menu", game.changeSceneTo(1), onePress=True)

    def draw(self, mousePos, mouseStatus):
        self.window.fill(color="black")
        l = self.button1.process(mousePos, mouseStatus)
        self.window.blit(l[0], l[1])
        