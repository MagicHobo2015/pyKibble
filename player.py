import pygame as pg
from pygame.sprite import Sprite
from spriteSheet import SpriteSheet
from animationTimer import AnimationTimer


class Player(Sprite):
    
    def __init__(self, game) -> None:
        super().__init__()
        # this gives access to basically everything.
        self.game = game
        self.filePath = "./assets/spriteSheets/cannon.png"
        
        self.spriteWidth = 32
        self.spriteHeight = 32
        self.rect = pg.Rect(self.game.screen.get_width() / 2, self.game.screen.get_height() / 2, self.spriteWidth, self.spriteHeight )
        self.color = pg.Color(0, 0, 0)
        self.spritesheet = SpriteSheet( self.filePath, self.spriteWidth, self.spriteHeight )
        self.animationList = self.spritesheet.getAllSprites()
        self.animationSpeed = 100
        self.animationTimer = AnimationTimer(self.animationList, self.animationSpeed, startIndex=0, loop=False)
        self.firing = False
        
    def move( self, moveTup ):
        self.rect.centerx += moveTup[0]
        self.rect.centery += moveTup[1]
        

    def draw(self, screen) -> None:
        # players location is SET here, not changed
        self.location = ( self.rect.centerx, self.rect.centery )

        imgToBlit = self.animationTimer.image()if self.firing else self.animationList[0]
        screen.blit(imgToBlit, self.location)