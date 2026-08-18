import pygame as pg

class Button:
    def __init__(self, x, y, width, height, buttonText='Button', fontsize = 40, onclickFunction=None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.fontsize = fontsize
        self.onclickFunction = onclickFunction
        self.clickableNow: bool = True
        self.alreadyPressed: bool = False
        self.animation: bool = False

        self.fillColors = {
            'normal': '#ffffff',
            'pressed': '#333333',
        }
        
        self.currentState = 'normal'
        self.needsRedraw = True 

        self.buttonSurface = pg.Surface((self.width, self.height))
        self.buttonRect = pg.Rect(self.x, self.y, self.width, self.height)
        self.buttonSurf = pg.font.SysFont('Arial', self.fontsize).render(buttonText, True, (20, 20, 20))
    
    def process(self, mousePos, mouseState): 
        self.buttonRect.x = self.x
        self.buttonRect.y = self.y
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

class imgButton(Button):
    def __init__(self, x, y, width, height, imgSrc, onclickFunction=None):
        super().__init__(x, y, width, height, onclickFunction=onclickFunction)
        self.buttonSurf = pg.transform.scale(pg.image.load(imgSrc).convert_alpha(), (self.width, self.height))

    def process(self, mousePos, mouseState):
        self.buttonRect.x = self.x
        self.buttonRect.y = self.y

        if self.buttonRect.collidepoint(mousePos) and (not mouseState[0]):
            self.clickableNow = True
        elif (not self.buttonRect.collidepoint(mousePos)) and mouseState[0]:
            self.clickableNow = False

        if self.buttonRect.collidepoint(mousePos) and self.clickableNow:
            if mouseState[0]:
                self.alreadyPressed = True
            elif self.alreadyPressed:
                if self.onclickFunction:
                    self.onclickFunction()
                self.alreadyPressed = False
        else:
            self.alreadyPressed = False
            
        return self.buttonSurf, self.buttonRect