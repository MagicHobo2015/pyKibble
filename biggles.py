import pygame as pg
from pygame.sprite import Sprite
from spriteSheet import SpriteSheet
from animationTimer import AnimationTimer

class Biggles( Sprite ):
    def __init__( self, game ) -> None:
        super().__init__()
        self.game = game
        self.foods = self.game.foods
        self.hitPoints = 50
        self.speed = self.game.settings.headSpeed
        self.direction = 1

        self.spriteWidth = 199
        self.spriteHeight = 233
        self.scale = 1
        self.delay = 100
        self.imgDir = "./assets/spriteSheets/bigglesHead.png"
        self.images = SpriteSheet( self.imgDir, self.spriteWidth, self.spriteHeight, self.game )
        self.biteimages = self.images.getAllSprites( self.scale )
        self.biteAnimationTimer = AnimationTimer( self.biteimages, self.delay, 0, False )

        self.rect = self.biteimages[0].get_rect()
        self.biting = False

    # called when a food collides with head
    def hit( self ):
        self.biting = True          
            
    def update(self):
        if self.biteAnimationTimer.isExpired():
            self.biting = False
            self.biteAnimationTimer.reset()
        if self.rect.centerx > self.game.screen.get_width() or self.rect.centerx < 0:
            self.direction *= -1
        self.rect.centerx = self.direction * self.speed + self.rect.centerx

        self.draw()


    def draw(self) -> None:
        imgToBlit = self.biteimages[0] if not self.biting else self.biteAnimationTimer.image()
        
        self.game.screen.blit( imgToBlit, self.rect.center )

