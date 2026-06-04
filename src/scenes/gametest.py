import pygame as pg
from util.button import Button
from scenes.scene import Scene

class GameTest(Scene):
    def __init__(self, width: int, height: int, game):
        super().__init__("wizardshut - options", width, height, game)
        self.button1 = Button(50, 50, 200, 70, "back to menu", lambda: game.changeSceneTo("MainMenu"))
        self.mesutimg = pg.transform.scale(pg.image.load('src/resources/img/mesut.png'), (100, 140))
        self.mesutpos:list[int,int] = [100,100]
        self.mesutspeed:list[int,int] = [0,0]

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
                    self.game.running = 0

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
            
            if self.RightArrow and self.LeftArrow: self.mesutspeed[0] = 0
            elif self.RightArrow: self.mesutspeed[0] = 10
            elif self.LeftArrow: self.mesutspeed[0] = -10
            else: self.mesutspeed[0] = 0
            
            if self.UpArrow and self.DownArrow: self.mesutspeed[1] = 0
            elif self.UpArrow: self.mesutspeed[1] = -10
            elif self.DownArrow: self.mesutspeed[1] = 10
            else: self.mesutspeed[1] = 0


    def update(self):
        self.game.updateMouse()
        self.checkEvents()
        self.draw(self.game.mousePos, self.game.mouseStatus)
        pg.display.update()
        self.game.clock.tick(60)

    def draw(self, mousePos, mouseStatus):
        self.window.fill(color="black")

        self.mesutpos[0] = min(max(self.mesutpos[0] + self.mesutspeed[0], 0), 540)
        self.mesutpos[1] = min(max(self.mesutpos[1] + self.mesutspeed[1], 0), 380)


        self.window.blit(self.mesutimg,(self.mesutpos[0], self.mesutpos[1]))
        mPos, mStat = self.button1.process(mousePos, mouseStatus)
        self.window.blit(mPos, mStat)

        

