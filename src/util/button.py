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
        
        self.currentState = 'normal'
        self.needsRedraw = True 

        self.buttonSurface = pg.Surface((self.width, self.height))
        self.buttonRect = pg.Rect(self.x, self.y, self.width, self.height)
        self.buttonSurf = pg.font.SysFont('Arial', 40).render(buttonText, True, (20, 20, 20))
    
    def process(self, mousePos, mouseState): 
        newState = 'normal'
        
        if self.buttonRect.collidepoint(mousePos) and (not mouseState[0]):
            self.clickableNow = True
        elif (not self.buttonRect.collidepoint(mousePos)) and mouseState[0]:
            self.clickableNow = False

        if self.buttonRect.collidepoint(mousePos) and self.clickableNow:
            if mouseState[0]:
                newState = 'pressed'
                self.alreadyPressed = True
            elif self.alreadyPressed:
                self.onclickFunction()
                self.alreadyPressed = False
        else:
            self.alreadyPressed = False
        
        if newState != self.currentState or self.needsRedraw:
            self.buttonSurface.fill(self.fillColors[newState])
            self.buttonSurface.blit(self.buttonSurf, [
                self.buttonRect.width/2 - self.buttonSurf.get_rect().width/2,
                self.buttonRect.height/2 - self.buttonSurf.get_rect().height/2
            ])
            self.currentState = newState
            self.needsRedraw = False
            
        return self.buttonSurface, self.buttonRect