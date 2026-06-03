import pygame as pg
from util.button import Button
from scenes.scene import Scene

class GameTest(Scene):
    def __init__(self, width: int, height: int, game):
        super().__init__("wizardshut - options", width, height, game)
        self.button1 = Button(50, 50, 200, 70, "back to menu", lambda: game.changeSceneTo("MainMenu"))
        self.mesutimg = pg.transform.scale(pg.image.load('src/resources/img/mesut.png'), (100, 140))
        self.mesutpos = [100,100]
        
    def checkEvents(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.game.running = False
        
            if event.type == pg.KEYDOWN:    
                if event.key == pg.K_q:
                    self.game.running = 0
                
                if event.key == pg.K_UP:
                    self.mesutpos[1] -= 10
                
                if event.key == pg.K_DOWN:
                    self.mesutpos[1] += 10
                
                if event.key == pg.K_RIGHT:
                    self.mesutpos[0] += 10

                if event.key == pg.K_LEFT:
                    self.mesutpos[0] -= 10

    def update(self):
        self.game.updateMouse()
        self.checkEvents()
        self.draw(self.game.mousePos, self.game.mouseStatus)
        pg.display.update()
        self.game.clock.tick(60)

    def draw(self, mousePos, mouseStatus):
        self.window.fill(color="black")

        mPos, mStat = self.button1.process(mousePos, mouseStatus)
        self.window.blit(mPos, mStat)

        self.window.blit(self.mesutimg,(self.mesutpos[0], self.mesutpos[1]))

