import pygame as pg
import os.path
import sys
from pygame.event import Event

WIDTH = 640
HEIGHT = 480
BG_COLOR = (20,50,50)

pg.init()
pg.display.init()
pg.display.set_caption('wizardshut')

window = pg.display.set_mode((WIDTH, HEIGHT), vsync=1)
clock = pg.time.Clock()

              
running: bool = True

def check_events(l: list[Event]):
    for event in l:
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        
        if event.type == pg.KEYDOWN:    
            if event.key == pg.K_q:
                pg.quit()
                sys.exit()
            '''
            if event.key == pg.K_UP:
                character.move_char(0,-10)
            if event.key == pg.K_DOWN:
                character.move_char(0,10)
            if event.key == pg.K_RIGHT:
                character.move_char(10,0)
            if event.key == pg.K_LEFT:
                character.move_char(-10,0)
            if event.key == pg.K_SPACE:
                character.char_shoot(window)
                print(bullets)'''

while running:                                                                                                    
    
    check_events(pg.event.get())


    pg.display.update()
    clock.tick(60)
