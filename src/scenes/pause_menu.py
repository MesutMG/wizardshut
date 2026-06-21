import pygame as pg
from util.button import Button
from util.button import imgButton
from scenes.scene import Scene

class PauseMenu(Scene):
    def __init__(self, width: int, height: int, game, sceneBelow):
        super().__init__("wizardshut - menu", width, height, game)
        self.sceneBelow = sceneBelow
        self.button1 = Button(x=width/2 - 100, y=50, width=200, height=100, buttonText="back to menu", fontsize=25, onclickFunction=lambda: game.changeSceneTo("MainMenu"))
        self.button2 = imgButton(x=width/2 - 100, y=200, width=200, height=100, imgSrc="src/resources/buttons/button_exit.png", onclickFunction=lambda: game.exit_game())
        self.button3 = imgButton(x=width/2 - 100, y=350, width=200, height=100, imgSrc="src/resources/buttons/button_play.png", onclickFunction=lambda: self.sceneBelow.setPaused(False))

    def checkEvents(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.game.running = False
        
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_q:
                    self.game.running = False

                if event.key == pg.K_ESCAPE:
                    self.sceneBelow.setPaused(False)


    def update(self):
        self.game.updateMouse()
        self.checkEvents()
        self.draw(self.game.mousePos, self.game.mouseStatus)

    def draw(self, mousePos, mouseStatus):
        self.window.fill("#55555555")

        btnSrf, btnRct = self.button2.process(mousePos, mouseStatus)
        self.window.blit(btnSrf, btnRct)

        btnSrf, btnRct = self.button3.process(mousePos, mouseStatus)
        self.window.blit(btnSrf, btnRct)
        
