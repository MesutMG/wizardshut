import pygame as pg
from util.button import Button
from scenes.scene import Scene

class GameTest(Scene):
    def __init__(self, width: int, height: int, game):
        super().__init__("wizardshut - options", width, height, game)
        self.button1 = Button(50, 50, 200, 70, "back to menu", lambda: game.changeSceneTo("MainMenu"))
        self.mesutimg = pg.transform.scale(pg.image.load('src/resources/img/mesut.png'), (100, 140))

    def update(self, game):
        game.updateMouse()
        game.checkEvents()
        self.draw(game.mousePos, game.mouseStatus)
        pg.display.update()
        game.clock.tick(60)

    def draw(self, mousePos, mouseStatus):
        self.window.fill(color="black")

        mPos, mStat = self.button1.process(mousePos, mouseStatus)
        self.window.blit(mPos, mStat)

