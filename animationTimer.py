import pygame as pg

class AnimationTimer:
    def __init__( self, imageList, delay=50, startIndex=0, loop=False ) -> None:
        # set my variables
        self.imageList = imageList
        self.endOfList = len(imageList)
        self.lastCalled = 0
        self.delay = delay
        self.loop = loop
        self.startIndex = startIndex
        self.index = self.startIndex
        
        
        # returns true if you have reached the end of an animation
    def isExpired(self) -> bool:
        return not self.loop and self.index >= self.endOfList - 1
        
        
        # returns the next frame of animation
    def nextFrame(self) -> None:
        if self.isExpired(): return
        now = pg.time.get_ticks()
        
        if now - self.lastCalled > self.delay:
            # here enough time has elapsed, increment'
            self.index += 1
            if self.loop: self.index %= self.endOfList
            print( self.index )
            self.lastCalled = now
        
        # starts the animation timer over
    def resetAnimationTimer(self) -> None:
        self.index = self.startIndex if self.startIndex <= self.endOfList else 0
    
    
        # returns the next image in a list of animations       
    def image(self) -> pg.surface:
        # increment the timer
        self.nextFrame()
        return self.imageList[self.index] if not self.isExpired() else None
