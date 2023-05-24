import pygame as pg
import os
import random


class Sound:
    def __init__(self) -> None:
        self.mixer = pg.mixer.init()
        
        self.shootSoundLocation = "./assets/sounds/shoot.flac"
        self.shootSound = pg.mixer.Sound( self.shootSoundLocation )
        
        self.splatSoundLocation = "./assets/sounds/impsplat"
        self.splatSounds = []
        
        
    def prepSplatSounds(self):
        for file in os.listdir( self.splatSoundLocation ):
            newSound = pg.mixer.Sound( f'{ self.splatSoundLocation }/{ file }' )
            self.splatSounds.append( newSound )
        
    def playShootSound(self):
        self.shootSound.play()
        
    
    def playSplatSound(self):
        index = random.randrange( 0, 3 )
        sound = self.splatSounds[index]
        sound.play()
        
    @staticmethod
    def testSounds():
        mixer = Sound()
        mixer.prepSplatSounds()
        mixer.playShootSound()
        
if __name__ == "__main__":
    Sound.testSounds()