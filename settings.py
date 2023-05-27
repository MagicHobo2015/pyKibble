class Settings:
    def __init__(self) -> None:
        # screen size set here
        self.resolution = [1920, 1080]
        self.bgColor = (132, 135, 133)
        
        self.debugging = True
        self.showFps = False
        self.playerCoordinates = False
        
        self.playerSpeed = 10
        self.foodSpeed = 5
        self.headSpeed = 5
