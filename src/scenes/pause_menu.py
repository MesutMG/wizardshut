import pygame as pg
from util.button import Button
from scenes.scene import Scene

class PauseMenu(Scene):
    def __init__(self, width: int, height: int, game, sceneBelow):
        super().__init__("wizardshut - menu", width, height, game)
        self.sceneBelow = sceneBelow
        self.button1 = Button(100, 20, 100, 50, "Main Menu", lambda: game.changeSceneTo("MainMenu"))
        self.button2 = Button(100, 200, 100, 50, "Exit", lambda: game.exit_game())
        self.button3 = Button(100, 380, 100, 50, "Game Test", lambda: game.changeSceneTo("GameTest"))

    def checkEvents(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.game.running = False
        
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_q:
                    self.game.running = 0

                if event.key == pg.K_ESCAPE:
                    self.sceneBelow.setPaused(False)


    def update(self):
        self.game.updateMouse()
        self.checkEvents()
        self.draw(self.game.mousePos, self.game.mouseStatus)

    def draw(self, mousePos, mouseStatus):
        pg.draw.rect(pg.Surface((640, 480), pg.SRCALPHA), (255, 255, 255, 128), (10, 10, 50, 50))
        self.window.blit(pg.Surface((640, 480), pg.SRCALPHA), (0, 0))
        
        btnSrf, btnRct = self.button1.process(mousePos, mouseStatus)
        self.window.blit(btnSrf, btnRct)

        btnSrf, btnRct = self.button2.process(mousePos, mouseStatus)
        self.window.blit(btnSrf, btnRct)

        btnSrf, btnRct = self.button3.process(mousePos, mouseStatus)
        self.window.blit(btnSrf, btnRct)
        
