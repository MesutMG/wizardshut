import pygame as pg
import os.path
import sys
from pygame.event import Event
from scenes.main_menu_scene import MainMenuScene
from scenes.options_scene import OptionsScene
from scenes.gametest import GameTest

WIDTH = 640
HEIGHT = 480

class Game:
    def __init__(self):
        self.gameScene = MainMenuScene(WIDTH, HEIGHT, self)
        self.scenes = {}
        self.clock = pg.time.Clock()
        self.running: bool = True
        self.mousePos = pg.mouse.get_pos()
        self.mouseStatus = pg.mouse.get_pressed()

    def updateMouse(self):
        self.mousePos = pg.mouse.get_pos()
        self.mouseStatus = pg.mouse.get_pressed()
        
    def changeSceneTo(self, sceneIndex):
        if self.scenes.get(sceneIndex) == None:
            self.createScene(sceneIndex)
            self.gameScene = self.scenes.get(sceneIndex)
        elif (self.gameScene == self.scenes.get(sceneIndex)):
            pass
        else:
            self.gameScene = self.scenes.get(sceneIndex)
    
    def createScene(self, sceneIndex):
        match sceneIndex:
            case "MainMenu":
                self.scenes["MainMenu"] = MainMenuScene(WIDTH, HEIGHT, self)
            
            case "Options":
                self.scenes["Options"] = OptionsScene(WIDTH, HEIGHT, self)

            case "GameTest":
                self.scenes["GameTest"] = GameTest(WIDTH, HEIGHT, self)

    def exit_game(self):
        self.running = False
            

pg.init()
pg.display.init()
game = Game()

while game.running:
    game.gameScene.update()

print("game end")
