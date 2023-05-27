import pygame as pg
import os
import random


class Sound:
    def __init__(self, game) -> None:
        self.mixer = pg.mixer.init()
        self.game = game
        
        self.shootSoundLocation = "./assets/sounds/shoot.flac"
        self.shootSound = pg.mixer.Sound( self.shootSoundLocation )
        
        self.splatSoundLocation = "./assets/sounds/impsplat"
        self.splatSounds = []
        
        self.backgroundMusicLocation = "./assets/sounds/backgroundMusic/happy.mp3"
        self.backgroundMusic = pg.mixer.music.load( self.backgroundMusicLocation )
        
        self.prepSplatSounds()
        
        
    def prepSplatSounds(self):
        for file in os.listdir( self.splatSoundLocation ):
            newSound = pg.mixer.Sound( f'{ self.splatSoundLocation }/{ file }' )
            self.splatSounds.append( newSound )
        if self.game.settings.debugging:
            print('Sound has been preped')
        
    def playShootSound(self):
        self.shootSound.play()
        
    def playbackgroundMusic( self ):
        pg.mixer.music.play( -1 )
    
    def playSplatSound(self):
        index = random.randrange( 0, 3 )
        sound = self.splatSounds[index]
        sound.play()
        
    # note this doesnt work, make better tests
    @staticmethod
    def testSounds():
        mixer = Sound()
        mixer.prepSplatSounds()
        mixer.playShootSound()
        
if __name__ == "__main__":
    Sound.testSounds()