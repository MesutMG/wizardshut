import pygame as pg

class Button:
    def __init__(self, x, y, width, height, buttonText='Button', onclickFunction=None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.onclickFunction = onclickFunction
        self.clickableNow: bool = True
        self.alreadyPressed: bool = False

        self.fillColors = {
            'normal': '#ffffff',
            'pressed': '#333333',
        }

        self.buttonSurface = pg.Surface((self.width, self.height))
        self.buttonRect = pg.Rect(self.x, self.y, self.width, self.height)
        self.buttonSurf = pg.font.SysFont('Arial', 40).render(buttonText, True, (20, 20, 20))
    
    def process(self, mousePos, mouseState): 
        self.buttonSurface.fill(self.fillColors['normal'])
        
        #if mouse is hovering
        if self.buttonRect.collidepoint(mousePos) and (not mouseState[0]):
            self.clickableNow = True

        #if clicking out of the button
        elif (not self.buttonRect.collidepoint(mousePos)) and mouseState[0]:
            self.clickableNow = False

        if self.buttonRect.collidepoint(mousePos) and self.clickableNow:
            if mouseState[0]:
                self.buttonSurface.fill(self.fillColors['pressed'])
                self.alreadyPressed = True

            elif self.alreadyPressed:
                self.onclickFunction()
                self.alreadyPressed = False
        else:
            self.alreadyPressed = False
        
        self.buttonSurface.blit(self.buttonSurf, [
            self.buttonRect.width/2 - self.buttonSurf.get_rect().width/2,
            self.buttonRect.height/2 - self.buttonSurf.get_rect().height/2
        ])
        return (self.buttonSurface, self.buttonRect)
