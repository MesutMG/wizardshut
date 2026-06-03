import pygame as pg

class Scene:
    def __init__(self, caption: str, width: int, height: int, game):
        pg.display.set_caption(caption)
        self.window = pg.display.set_mode((width, height), vsync=1)
        self.game = game

    def update(self, game):
        game.updateMouse()
        game.checkEvents()
        self.draw(game.mousePos, game.mouseStatus)
        pg.display.update()
        game.clock.tick(60)

    def draw(self, mousePos: tuple[int ,int], mouseStatus: tuple[bool, bool, bool]):
        self.window.fill(color="blue")

        