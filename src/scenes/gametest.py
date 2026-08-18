import pygame as pg
from util.button import Button
from scenes.scene import Scene
from characters.player import imgPlayer
from characters.npc import Npc

from scenes.pause_menu import PauseMenu

class GameTest(Scene):
    def __init__(self, width: int, height: int, game):
        super().__init__("wizardshut - options", width, height, game)
        self.pauseMenu: PauseMenu
        self.paused: bool = False
        self.button1 = Button(x=50, y=50, width=200, height=70, fontsize=20, buttonText="back to menu", onclickFunction=lambda: game.changeSceneTo("MainMenu"))
        
        self.mesut = imgPlayer(x=100, y=100, width=120, height=200, imgSrc='src/resources/img/mesut.png')
        self.npc1 = Npc(x=200, y=200, width=80, height=120, imgSrc='src/resources/img/npc.png')

        self.RightArrow:bool = False
        self.LeftArrow:bool = False
        self.UpArrow:bool = False
        self.DownArrow:bool = False
        
        
    def checkEvents(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.game.running = False
        
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_q:
                    self.game.running = False

                if event.key == pg.K_ESCAPE:
                    self.pauseGame()

                if event.key == pg.K_RIGHT:
                    self.RightArrow = True
                if event.key == pg.K_LEFT:
                    self.LeftArrow = True
                if event.key == pg.K_UP:
                    self.UpArrow = True
                if event.key == pg.K_DOWN:
                    self.DownArrow = True

            if event.type == pg.KEYUP:
                if event.key == pg.K_RIGHT:
                    self.RightArrow = False
                if event.key == pg.K_LEFT:
                    self.LeftArrow = False
                if event.key == pg.K_UP:
                    self.UpArrow = False
                if event.key == pg.K_DOWN:
                    self.DownArrow = False
            
        if self.RightArrow and self.LeftArrow: self.mesut.playerSpeed[0] = 0
        elif self.RightArrow: self.mesut.playerSpeed[0] = 5
        elif self.LeftArrow: self.mesut.playerSpeed[0] = -5
        else: self.mesut.playerSpeed[0] = 0
        
        if self.UpArrow and self.DownArrow: self.mesut.playerSpeed[1] = 0
        elif self.UpArrow: self.mesut.playerSpeed[1] = -5
        elif self.DownArrow: self.mesut.playerSpeed[1] = 5
        else: self.mesut.playerSpeed[1] = 0

    def draw(self, mousePos, mouseStatus):
        self.window.fill(color="green")

        self.window.blit(self.npc1.npcImg,(self.npc1.npcPos[0], self.npc1.npcPos[1]))

        self.mesut.playerPos[0] = min(max(self.mesut.playerPos[0] + self.mesut.playerSpeed[0], 0), 540)
        self.mesut.playerPos[1] = min(max(self.mesut.playerPos[1] + self.mesut.playerSpeed[1], 0), 340)
        self.window.blit(self.mesut.playerImg,(self.mesut.playerPos[0], self.mesut.playerPos[1]))
        
        mPos, mStat = self.button1.process(mousePos, mouseStatus)
        self.window.blit(mPos, mStat)

    def update(self):
        if self.paused:
            self.pauseMenu.update()
            print("Paused")
        else:
            print("Running")
            self.game.updateMouse()
            self.checkEvents()
            self.draw(self.game.mousePos, self.game.mouseStatus)

    def setPaused(self, v: bool):
        self.paused = v

    def pauseGame(self):
        self.paused = True
        self.RightArrow = False
        self.LeftArrow = False
        self.UpArrow = False
        self.DownArrow = False
        self.pauseMenu = PauseMenu(self.width, self.height, self.game, self)
'''
    def checkInteraction(self):
        if self.mesut.playerInteractionRect.colliderect(self.npc1.npcInteractionRect):
            print("foiwjf093jf")'''