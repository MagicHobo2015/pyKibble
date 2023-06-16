# 2d Platformer, trying to keep it as clean as i can

import pygame as pg
from settings import Settings
from vector import Vector
from biggles import Biggles
import sys


class Game:
    def __init__(self) -> None:
        # fireUp pygame
        pg.init()
        self.settings = Settings()
        self.screen = pg.display.set_mode(self.settings.resolution)
        pg.display.set_caption("Biggles Odyssey")
        self.running = True
        self.Fps_clock = pg.time.Clock()
        self.biggles = Biggles(self.screen, "biggles")
       
       
    def handle_events(self):
        directionKeys = {pg.K_UP: Vector(0, -1), pg.K_w: Vector(0, -1),
                         pg.K_s: Vector(0, 1), pg.K_DOWN: Vector(0, 1),
                         pg.K_a: Vector(-1, 0), pg.K_LEFT: Vector(-1, 0),
                         pg.K_d: Vector(1, 0), pg.K_RIGHT: Vector(1, 0)}

        # capture quit event
        for event in pg.event.get():
            if event.type == pg.QUIT:
                # user wants out of program
                self.shutdown_game()

        keys_pressed = pg.key.get_pressed()
        for key in directionKeys:
            if keys_pressed[key]:
                self.biggles.move(directionKeys[key])        

    def shutdown_game(self) -> None:
        self.running = False
        # maybe goodbye music
        pg.quit()
        sys.exit()

    def update(self) -> None:
        self.screen.fill(self.settings.bg_color)
        self.biggles.update()
        pg.display.flip()
        # keep it at 60 for consistent results.
        self.Fps_clock.tick(60)
        if self.settings.show_fps:
            print(self.Fps_clock.get_fps())
    
    def play(self):
        # start the music here @ half volume
        # start the title menu
        
        while self.running:
            self.handle_events()
            self.update()
            pg.display.update()
    
def main() -> None:
    game = Game()
    game.play()
    
if __name__ == "__main__":
    main()