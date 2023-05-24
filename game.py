"""****************************************************************************  
*                   ____  __._____.  ___.   .__                               *
*    ______ ___.__.|    |/ _|__\_ |__\_ |__ |  |   ____                       *
*    \____ <   |  ||      < |  || __ \| __ \|  | _/ __ \                      *
*    |  |_> >___  ||    |  \|  || \_\ \ \_\ \  |_\  ___/                      *
*    |   __// ____||____|__ \__||___  /___  /____/\___  >                     *
*    |__|   \/             \/       \/    \/          \/                      *
*                                                                             *
*                                                                             *
*   Description: This is my python implementation of Feed Biggles Kibble      *
*                   You just shoot the kibble, (food), at biggles.            *
*   Author: Joshua Land                                                       *
*   Contact:                                                                  *
****************************************************************************"""
import pygame as pg
from settings import Settings
from player import Player
from food import Foods
from sound import Sound
import sys


class Game:
    def __init__(self) -> None:
        # this sets up pygame
        pg.init()
        self.settings = Settings()
        # window size set in settings.
        self.screen = pg.display.set_mode(self.settings.resolution)
        pg.display.set_caption("pyKibble")
        
        # for fps limits.
        self.clock = pg.time.Clock()
        self.running = True
        self.player = Player(self)
        
        # stuff to track
        self.foods = Foods(self)
        self.sounds = Sound()
        

    def checkEvents(self) -> None:
        # just a list of keys and what to do with them when pressed
        keyList = { pg.K_w: ( 0, -1 ), pg.K_s: ( 0 , 1 ), pg.K_d: ( 1, 0 ), pg.K_a: ( -1, 0 ),
                   pg.K_UP: ( 0, -1 ), pg.K_DOWN: ( 0, 1 ), pg.K_RIGHT: ( 1, 0 ), pg.K_LEFT: ( -1, 0 ) }
        secondaryKeys = { pg.K_SPACE: "A", pg.K_RETURN: "Start" }
        
        # first look for quit event TODO: convert all this to use keypressed so we can have two things pressed at once
        for event in pg.event.get():
            if event.type == pg.QUIT:
                # do the clean up stuff here
                self.shutDownGame()   
            elif event.type == pg.KEYDOWN:
                if event.key in keyList:
                    self.player.move(keyList[event.key], pg.KEYDOWN)
                elif event.key in secondaryKeys:
                    # handel start press and "a" button
                    if secondaryKeys[event.key] == "A":
                        self.player.fire(True)
                    elif secondaryKeys[event.key] == "Start":
                        if self.running:
                            self.pause()
                        # TODO: More here like menu selection, game start ect...
            elif event.type == pg.KEYUP:
                if event.key in keyList:
                    self.player.move(keyList[event.key], pg.KEYUP)
                elif event.key in secondaryKeys:
                    if secondaryKeys[event.key] == "A":
                        pass


    def pause(self):
        pass
    
    
    # shutdown clean up
    def shutDownGame(self) -> None:
        # clean up pygame
        pg.display.quit()
        pg.quit()
        sys.exit()

    # All drawing is called from here.
    def update(self) -> None:
        # clear the screen
        self.screen.fill(self.settings.bgColor)
        self.player.update( self.screen )
        self.foods.update()


        # flip the display
        pg.display.flip()


    # main game loop is here
    def play(self) -> None:
        while self.running:
            self.checkEvents()

            if self.settings.showFps:
                print(self.clock.get_fps())

            self.update()
            pg.display.update()
            # limit frames per-second so it runs the same speed with different
            # hardware
            self.clock.tick(60)


def main():
    game = Game()
    game.play()


if __name__ == "__main__":
    main()