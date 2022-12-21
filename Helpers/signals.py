class Signal : 
    def __init__(self, pos : int, red : int, yel : int, gre : int) -> None:
        self.pos = pos 
        self.red = red
        self.yel = yel
        self.gre = gre
        self.cycle = red + yel + gre

    def calc_dist(self, pos_2 : int) -> int:
        return self.pos - pos_2 if pos_2 < self.pos else -1