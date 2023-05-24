"""****************************************************************************  
*   Description: Just a class to handle my sprite sheets.
*   Note: Food sheet 16 x 15
*
*****************************************************************************"""

import pygame as pg


class SpriteSheet:
    def __init__( self, filepath, spriteWidth, spriteHeight ) -> None:
        try:
            # load the file
            self.file = open(filepath, "r")

        except (OSError, IOError) as error:
            print(f"Something went Wrong with your file, {error}")  
 
        self.spriteSheet = pg.image.load(self.file).convert_alpha()

        # release the file
        self.file.close()
        
        self.spriteX = 0
        self.spriteY = 0
        self.spriteWidth = spriteWidth
        self.spriteheight = spriteHeight
        
        self.currentXOffset = 32
        self.currentYOffset = 32
        
        self.rectangle = pg.Rect( self.spriteX, self.spriteY, self.spriteWidth, self.spriteheight )
        
        self.listOfSprites = []
        
    def getAllSprites(self):
        yEnd = int((self.spriteSheet.get_height() / self.currentYOffset))
        xEnd = int((self.spriteSheet.get_width() / self.currentXOffset))
        
        for y in range( 0, yEnd ):
            yLocation = self.currentYOffset * y
            
            for x in range( 0, xEnd ):
                xLocation = self.currentXOffset * x
                
                self.captureSquare = pg.Rect( xLocation,
                                     yLocation, self.spriteWidth,
                                     self.spriteheight )

                # new surface for the sprite
                image = pg.Surface( (self.spriteWidth*3, self.spriteheight*3), pg.SRCALPHA )
                image.blit( self.spriteSheet, self.rectangle, self.captureSquare ) 
                # now scale
                stretched = pg.transform.rotozoom(image, 0, 3)
                self.listOfSprites.append( stretched )      
        return self.listOfSprites
    
    
    @staticmethod
    def tests():
        spritesheet = SpriteSheet( "./assets/spriteSheets/cannon.png", 0, 0, 32, 32 )
        images = spritesheet.getAllSprites()
        print(images[0])
        
                     
if __name__ == "__main__":
    # run test
    SpriteSheet.tests()
