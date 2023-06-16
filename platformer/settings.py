import pygame as pg


class Settings:
    def __init__(self) -> None:
        self.resolution = (1200, 800)
        self.music_volume = .50
        self.fx_volume = .5
        self.bg_color = (137, 207, 240)
        self.debug = True
        self.show_fps = False # True
        