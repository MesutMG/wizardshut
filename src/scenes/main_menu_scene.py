import pygame as pg
from util.button import Button
from scenes.scene import Scene

class MainMenuScene(Scene):
    def __init__(self, width: int, height: int, game):
        super().__init__("wizardshut - menu", width, height, game)
        self.button1 = Button(20, 20, 100, 50, "options", lambda: game.changeSceneTo("Options"))
        self.button2 = Button(80, 80, 100, 50, "exit", lambda: game.exit_game())
        self.button3 = Button(120, 120, 100, 50, "gametest", lambda: game.changeSceneTo("GameTest"))

    def draw(self, mousePos, mouseStatus):
        self.window.fill(color="orange")
        
        btnSrf, btnRct = self.button1.process(mousePos, mouseStatus)
        self.window.blit(btnSrf, btnRct)

        btnSrf, btnRct = self.button2.process(mousePos, mouseStatus)
        self.window.blit(btnSrf, btnRct)

        btnSrf, btnRct = self.button3.process(mousePos, mouseStatus)
        self.window.blit(btnSrf, btnRct)
        
