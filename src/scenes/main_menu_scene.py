import pygame as pg
from util.button import Button
from scenes.scene import Scene

class MainMenuScene(Scene):
    def __init__(self, width: int, height: int, game):
        super().__init__("wizardshut - menu", width, height, game)
        self.buttons = []
        self.button1 = Button(20, 20, 100, 50, "options", lambda: game.changeSceneTo(2))

    def draw(self, mousePos, mouseStatus):
        self.window.fill(color="orange")
        l = self.button1.process(mousePos, mouseStatus)
        self.window.blit(l[0], l[1])
