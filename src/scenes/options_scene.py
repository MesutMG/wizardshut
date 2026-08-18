import pygame as pg
from util.button import Button
from scenes.scene import Scene

class OptionsScene(Scene):
    def __init__(self, width: int, height: int, game):
        super().__init__("wizardshut - options", width, height, game)
        self.button1 = Button(x=width/2 - 100, y=50, width=200, height=100, buttonText="back to menu", fontsize=25, onclickFunction=lambda: game.changeSceneTo("MainMenu"))
        self.oscarimg = pg.image.load('src/resources/img/oscar.png')

    def update(self):
        self.game.updateMouse()
        self.checkEvents()
        self.draw(self.game.mousePos, self.game.mouseStatus)

    def draw(self, mousePos, mouseStatus):
        self.window.fill(color="black")

        mPos, mStat = self.button1.process(mousePos, mouseStatus)
        self.window.blit(mPos, mStat)

        self.window.blit(self.oscarimg,(10, 10))