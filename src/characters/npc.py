import pygame as pg
from characters.character import Character

class Npc(Character):
    def __init__(self, x, y, width, height, imgSrc):
        super().__init__(x, y, width, height)
        #self.interactionDistance: int = interactionDistance
        self.imgSrc = imgSrc
        self.npcImg = pg.transform.scale(pg.image.load(self.imgSrc), (self.width, self.height))
        #self.npcInteractionRect = pg.Rect((self.x - self.interactionDistance, self.y - interactionDistance/2), (self.width + interactionDistance*2, self.height + interactionDistance))
        self.npcPos:list[int,int] = [x, y]
        self.npcSpeed:list[int,int] = [0,0]
