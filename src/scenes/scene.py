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
                '''
                if event.key == pg.K_UP:
                    move_char(0,-10)
                
                if event.key == pg.K_DOWN:
                    move_char(0,10)
                
                if event.key == pg.K_RIGHT:
                    character.move_char(10,0)
                if event.key == pg.K_LEFT:
                    character.move_char(-10,0)
                if event.key == pg.K_SPACE:
                    character.char_shoot(window)
                    print(bullets)'''
                
    def update(self):
        self.game.updateMouse()
        self.checkEvents()
        self.draw(self.game.mousePos, self.game.mouseStatus)
        pg.display.update()
        self.game.clock.tick(60)

    def draw(self, mousePos: tuple[int ,int], mouseStatus: tuple[bool, bool, bool]):
        self.window.fill(color="blue")

        
