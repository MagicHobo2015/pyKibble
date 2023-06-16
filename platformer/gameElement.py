import pygame as pg
from vector import Vector
from abc import ABC, abstractmethod

class GameElement(ABC):
    def __init__(self, game_screen: pg.Surface, type: str) -> None:
        super().__init__()
        self.game_screen = game_screen
        self.vector = Vector(0, 0)
        self.rect = pg.Rect( 0, 0, 32, 32 )
        self.type = type
        self.spriteSpecs = {}
        self.animations = {}

    def get_type(self) -> str:
        return self.type

    def set_type(self, type: str) -> None:
        self.type = type

    @abstractmethod
    def update(self) -> None:
        pass

    @abstractmethod
    def draw(self) -> None:
        pass