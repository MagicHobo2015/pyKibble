from pygame.surface import Surface
from actor import Actor
import pygame as pg

from vector import Vector

class Biggles( Actor ):
    def __init__( self, game_screen: Surface, type: str ) -> None:
        super().__init__( game_screen, type )
        self.color = pg.Color( 0, 255, 0 )
        self.game_screen = game_screen
        self.type = type

    def jump( self ) -> None:
        pass

    def duck( self ) -> None:
        pass
    
    def attack( self ) -> None:
        pass

    def move( self, deltaLocation: Vector ) -> None:
        return super().move( deltaLocation )         

    def update(self) -> None:
        self.draw()

    def draw(self) -> None:
        pg.draw.rect( self.game_screen, self.color, self.rect )