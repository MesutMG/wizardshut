import pygame as pg
from util.button import Button
from util.button import imgButton
from scenes.scene import Scene

class MainMenuScene(Scene):
    def __init__(self, width: int, height: int, game):
        super().__init__("wizardshut - menu", width, height, game)
        self.button1 = imgButton(220, 50, 200, 100, "src/resources/buttons/button_save.png", lambda: game.changeSceneTo("Options"))
        self.button2 = imgButton(220, 200, 200, 100, "src/resources/buttons/button_exit.png", lambda: game.exit_game())
        self.button3 = imgButton(220, 350, 200, 100, "src/resources/buttons/button_play.png", lambda: game.changeSceneTo("GameTest"))

    def draw(self, mousePos, mouseStatus):
        self.window.fill(color="orange")
        
        btnSrf, btnRct = self.button1.process(mousePos, mouseStatus)
        self.window.blit(btnSrf, btnRct)

        btnSrf, btnRct = self.button2.process(mousePos, mouseStatus)
        self.window.blit(btnSrf, btnRct)

        btnSrf, btnRct = self.button3.process(mousePos, mouseStatus)
        self.window.blit(btnSrf, btnRct)
        
