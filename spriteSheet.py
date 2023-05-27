"""****************************************************************************  
*   Description: Just a class to handle my sprite sheets.
*   Note: Food sheet 16 x 16, biggles head 200 x 230
*
*****************************************************************************"""

import pygame as pg

class SpriteSheet:
    def __init__( self, filepath, spriteWidth, spriteHeight, game ) -> None:
        try:
            # load the file
            self.file = open(filepath, "r")

        except (OSError, IOError) as error:
            print(f"Something went Wrong with your file, {error}")  
 
        self.spriteSheet = pg.image.load(self.file).convert_alpha()
        self.game = game

        # release the file
        self.file.close()
        
        self.spriteX = 0
        self.spriteY = 0
        self.spriteWidth = spriteWidth
        self.spriteheight = spriteHeight       

        self.rectangle = pg.Rect( self.spriteX, self.spriteY, self.spriteWidth, self.spriteheight )

        self.listOfSprites = []

    def getAllSprites(self, scale):
        yEnd = int((self.spriteSheet.get_height() / self.spriteheight))
        xEnd = int((self.spriteSheet.get_width() / self.spriteWidth))

        if self.game.settings.debugging:
            print(f"spritesheet has { xEnd }, Columns")
            print(f"spritesheet has { yEnd }, Rows")
        for y in range( 0, yEnd ):
            yLocation = self.spriteWidth * y
    
            for x in range( 0, xEnd ):
                xLocation = self.spriteheight * x
                
                self.captureSquare = pg.Rect( xLocation,
                                     yLocation, self.spriteWidth,
                                     self.spriteheight )

                # new surface for the sprite
                image = pg.Surface( (self.spriteWidth, self.spriteheight), pg.SRCALPHA )
                image.blit( self.spriteSheet, self.rectangle, self.captureSquare ) 
                # now scale
                stretched = pg.transform.rotozoom(image, 0, scale)
                self.listOfSprites.append( stretched )      
        return self.listOfSprites
    
    
    @staticmethod
    def tests():
        spritesheet = SpriteSheet( "./assets/spriteSheets/cannon.png", 32, 32 )
        images = spritesheet.getAllSprites()
        print(images[0])
        
                     
if __name__ == "__main__":
    # run test
    SpriteSheet.tests()
