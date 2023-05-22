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
from player import Player
import sys
from settings import Settings

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

    def checkEvents(self) -> None:
        
        keyList = { pg.K_w: ( 0, -1 ), pg.K_s: ( 0 , 1 ), pg.K_d: ( 1, 0 ), pg.K_a: ( -1, 0 ) }

        # first look for quit event
        for event in pg.event.get():
            if event.type == pg.QUIT:
                # do the clean up stuff here
                self.shutDownGame()
            elif event.type == pg.KEYDOWN:
                self.player.move(keyList[event.key])

    # shutdown clean up
    def shutDownGame(self) -> None:
        # clean up pygame
        pg.display.quit()
        pg.quit()
        sys.exit()

    # All drawing is called from here.
    def draw(self) -> None:
        # clear the screen
        self.screen.fill(self.settings.bgColor)
        self.player.draw(self.screen)
        
        # flip the display
        pg.display.flip()


    # main game loop is here
    def play(self) -> None:
        while self.running:
            self.checkEvents()

            if self.settings.showFps:
                print(self.clock.get_fps())

            self.draw()
            pg.display.update()
            # limit frames per-second so it runs the same speed with different
            # hardware
            self.clock.tick(60)


def main():
    game = Game()
    game.play()
    
    
if __name__ == "__main__":
    main()