import pygame as pg
import os.path
import sys
from pygame.event import Event
from main_menu import MainMenu

WIDTH = 640
HEIGHT = 480

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

mainmenu = MainMenu()

while running:
    mousePos = pg.mouse.get_pos()
    mouseStatus = pg.mouse.get_pressed()

    check_events(pg.event.get())

    mainmenu.draw(window, mousePos, mouseStatus)

    pg.display.update()
    clock.tick(60)
