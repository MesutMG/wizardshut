import pygame as pg
import os.path
import sys
from pygame.event import Event
from scenes.main_menu_scene import MainMenuScene
from scenes.options_scene import OptionsScene

WIDTH = 640
HEIGHT = 480

class Game:
    def __init__(self):
        self.gameScene = MainMenuScene(WIDTH, HEIGHT, self)
        self.sceneName = 0 #none
        self.scenes = {}
        self.clock = pg.time.Clock
        self.running: bool = True
        self.mousePos = pg.mouse.get_pos()
        self.mouseStatus = pg.mouse.get_pressed()

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
        
            if event.type == pg.KEYDOWN:    
                if event.key == pg.K_q:
                    self.running = 0
                
                if event.key == pg.K_UP:
                    self.changeSceneTo(1) #.move_char(0,-10)
                
                if event.key == pg.K_DOWN:
                    self.changeSceneTo(2)#character.move_char(0,10)
                '''
                if event.key == pg.K_RIGHT:
                    character.move_char(10,0)
                if event.key == pg.K_LEFT:
                    character.move_char(-10,0)
                if event.key == pg.K_SPACE:
                    character.char_shoot(window)
                    print(bullets)'''

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
            case 1:
                self.scenes[1] = MainMenuScene(WIDTH, HEIGHT)
            
            case 2:
                self.scenes[2] = OptionsScene(WIDTH, HEIGHT)
            

pg.init()
pg.display.init()
game = Game()

while game.running:
    game.updateMouse()
    game.check_events()

    game.gameScene.draw(game.mousePos, game.mouseStatus)

    pg.display.update()
    game.clock.tick(60)
    
print("game end")