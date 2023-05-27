import pygame as pg
from pygame.sprite import Sprite 
from spriteSheet import SpriteSheet
from random import randrange


# this class handles rendering, movement, and images
class Food(Sprite):
    def __init__( self, game, spawnLocation ) -> None:
        super().__init__()
        self.active = True
        self.game = game
        self.speed = self.game.settings.foodSpeed
        
        self.scale = 3
        self.spriteSize = 16
        self.image = SpriteSheet( "./assets/spriteSheets/Food.png", self.spriteSize, self.spriteSize, self.game )
        self.image = self.image.getAllSprites( self.scale )
        self.rect = self.image[0].get_rect()
        self.rect.center = spawnLocation

        self.type = randrange(0, len(self.image))
        self.isFoodExpired = False

    def update(self):
        # Movement happens here, TODO: add horizontal velocity
        self.rect.center = ( self.rect.centerx, self.rect.centery - self.speed )
        self.draw( self.game.screen )

    def isExpired(self):
        return self.isFoodExpired

    def hit(self, food):
        food.isFoodExpired = True
        
    
    def draw(self, screen):
        imgToBlit = self.image[ self.type ]
        if self.rect.centery < 0:
            self.isFoodExpired = True
        screen.blit(imgToBlit, self.rect.center)
    

class Foods:
    def __init__( self, game ) -> None:
        self.foods = pg.sprite.Group()
        self.game = game
        
        self.listOfFood = []
        self.fireRate = 350
        self.lastFired = 0

    def update(self):
        for food in self.listOfFood:
            if food.isExpired():
                self.foods.remove( food )
                self.listOfFood.remove( food )
                self.game.sounds.playSplatSound()
        self.foods.update()

    def shoot(self, location):
        now = pg.time.get_ticks()
        if now - self.lastFired > self.fireRate:
            newFood = Food(self.game, location)
            self.foods.add( newFood )
            self.listOfFood.append( newFood )
            self.game.sounds.playShootSound()
            self.lastFired = now
        