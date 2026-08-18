import pygame as pg
from util.button import Button
from util.button import imgButton
from scenes.scene import Scene


def ease_in_cubic(t: float) -> float:
    return t * t * t

def ease_out_cubic(t: float) -> float:
    return 1 - (1 - t) ** 3

class MainMenuScene(Scene):
    def __init__(self, width: int, height: int, game):
        super().__init__("wizardshut - menu", width, height, game)
        self.nextScene = None
        self.animating = False
        self.activeButton = None

        self.animation_progress = 0.0
        self.animation_duration = 0.45
        self.start_x = 0
        self.target_x = 0

        self.button1 = imgButton(220, 50, 200, 100, "src/resources/buttons/button_save.png", 
                                 lambda: self.startTransition(self.button1, "Options", slide_to="right"))
        self.button2 = imgButton(220, 200, 200, 100, "src/resources/buttons/button_exit.png", 
                                 lambda: self.startTransition(self.button2, "Exit", slide_to="left"))
        self.button3 = imgButton(220, 350, 200, 100, "src/resources/buttons/button_play.png", 
                                 lambda: self.startTransition(self.button3, "GameTest", slide_to="left"))

    def startTransition(self, button, targetScene: str, slide_to: str = "left"):
        if not self.animating:
            self.animating = True
            self.nextScene = targetScene
            self.activeButton = button
            self.animation_progress = 0.0

            self.start_x = button.x

            if slide_to == "right":
                self.target_x = self.width + 50
            else:
                self.target_x = -button.width - 50

    def update(self):
        self.game.updateMouse()
        self.checkEvents()

        if self.animating:
            self.handleAnimation()

        self.draw(self.game.mousePos, self.game.mouseStatus)

    def handleAnimation(self):
        dt = 1.0 / 60.0
        self.animation_progress += dt / self.animation_duration

        if self.animation_progress >= 1.0:
            self.animation_progress = 1.0
            self.activeButton.x = self.target_x

            if self.nextScene == "Exit":
                self.game.running = False
            else:
                nextScene = self.nextScene
                self.animating = False
                self.activeButton = None
                self.game.changeSceneTo(nextScene)
        else:
            eased_t = ease_in_cubic(self.animation_progress)
            self.activeButton.x = self.start_x + (self.target_x - self.start_x) * eased_t

    def draw(self, mousePos, mouseStatus):
        self.window.fill(color="orange")

        currentMouseStatus = (False, False, False) if self.animating else mouseStatus

        btnSrf, btnRct = self.button1.process(mousePos, currentMouseStatus)
        self.window.blit(btnSrf, btnRct)

        btnSrf, btnRct = self.button2.process(mousePos, currentMouseStatus)
        self.window.blit(btnSrf, btnRct)

        btnSrf, btnRct = self.button3.process(mousePos, currentMouseStatus)
        self.window.blit(btnSrf, btnRct)
        