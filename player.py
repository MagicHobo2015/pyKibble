import pygame as pg
from pygame.sprite import Sprite
from spriteSheet import SpriteSheet
from animationTimer import AnimationTimer
from food import Foods


class Player(Sprite):
    
    def __init__(self, game) -> None:
        super().__init__()
        # this gives access to basically everything.
        self.game = game
        self.filePath = "./assets/spriteSheets/cannon.png"
        
        self.spriteWidth = 32
        self.spriteHeight = 32
        self.rect = pg.Rect(self.game.screen.get_width() / 2, self.game.screen.get_height() / 2, self.spriteWidth, self.spriteHeight )
        
        # animation vars
        self.spritesheet = SpriteSheet( self.filePath, self.spriteWidth, self.spriteHeight )
        self.animationList = self.spritesheet.getAllSprites()
        self.animationSpeed = 50
        self.animationTimer = AnimationTimer(self.animationList, self.animationSpeed, startIndex=0, loop=False)
        self.firing = False
        
        # movement vars
        self.speed = self.game.settings.playerSpeed
        self.moving = False
        self.verticalClamp = 815
        self.direction = ( 0, 0 )
        
        self.food = None
        
    def move( self, direction, upOrDown ) -> None:
        if upOrDown == pg.KEYDOWN:
            self.moving = True
            self.direction = direction
        elif upOrDown == pg.KEYUP:
            self.moving = False
            self.direction = ( 0, 0 )


    def update( self, game ) -> None:
        if self.animationTimer.isExpired():
            self.firing = False
            self.animationTimer.reset()
            
        if self.moving == True:
            self.rect.centerx += self.direction[0] * self.speed
            self.rect.centery += self.direction[1] * self.speed
        self.rect.center = self.clamp( self.rect.center )
        self.draw( game )
        

    def draw(self, screen) -> None:
        if self.food: self.food.update()
        imgToBlit = self.animationTimer.image() if self.firing and not self.animationTimer.isExpired() else self.animationList[0]
        screen.blit(imgToBlit, self.rect.center)


    def clamp(self, location) -> tuple:
        if self.game.settings.debugging and self.game.settings.playerCoordinates:
            print(f"Location is: { location }")
        
        tempX = max( 0, min(location[0], self.game.screen.get_width() - self.rect.width))
        tempY = max( self.verticalClamp, min(location[1], self.game.screen.get_height() - self.rect.height * 2))
        return ( tempX, tempY )

    
    def fire(self, fire) -> None:
        if fire and self.animationTimer.isExpired(): self.animationTimer.reset()
        self.firing = fire
        self.food = self.game.foods.shoot( self.rect.center )
        
        