import pygame as pg
from characters.character import Character

class imgPlayer(Character):
    def __init__(self, x, y, width, height, imgSrc='0'):
        super().__init__(x, y, width, height)
        self.imgSrc:str = imgSrc
        self.playerImg = pg.transform.scale(pg.image.load(self.imgSrc), (self.width,self.height))
        self.playerPos:list[int,int] = [self.x,self.y]
        self.playerSpeed:list[int,int] = [0,0]
