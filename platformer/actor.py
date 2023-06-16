import pygame as pg
from pygame.surface import Surface
from pygame.sprite import Sprite
from abc import ABC, abstractmethod
from vector import Vector

from gameElement import GameElement

class Actor( GameElement, ABC, Sprite ):
    def __init__(self, game_screen: Surface, type: str) -> None:
        super().__init__(game_screen, type)
        self.speed = 0
        self.direction = 0
        
    def move( self, deltaLoc: Vector ) -> None:
        # gotta catch this for physics
        self.vector += deltaLoc
        self.rect.centerx = self.vector.x
        self.rect.centery = self.vector.y

    def get_speed( self ) -> float:
        return self.speed

    def get_direction( self ) -> int:
        return self.direction

    def set_speed( self, speed: int ) -> None:
        self.speed = speed

    def set_direction(self, direction: int) -> None:
        self.direction = direction
        
    @abstractmethod
    def jump( self ) -> None:
        pass
    
    @abstractmethod
    def duck( self ) -> None:
        pass
    
    @abstractmethod
    def attack(self) -> None:
        pass