import pygame as pg

class Scene:
    def __init__(self, caption: str, width: int, height: int, game):
        pg.display.set_caption(caption)
        self.window = pg.display.set_mode((width, height), vsync=1)
        self.game = game

    def checkEvents(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.game.running = False
        
            if event.type == pg.KEYDOWN:    
                if event.key == pg.K_q:
                    self.game.running = 0
                
    def update(self):
        self.game.updateMouse()
        self.checkEvents()
        self.draw(self.game.mousePos, self.game.mouseStatus)

    def draw(self, mousePos: tuple[int ,int], mouseStatus: tuple[bool, bool, bool]):
        self.window.fill(color="blue")

        
