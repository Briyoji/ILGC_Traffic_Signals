class Car : 
    def __init__(self, pos: int, speed: int, mode: int) -> None:
        '''
            speed -> Velocity of car in km/h
        '''
        
        self.speed = speed 
        self.pos = pos 
        self.mode = mode 

    def update_pos(self, time : int = 1) :
        self.pos += self.speed * time
