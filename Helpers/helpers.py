from Helpers.car import *
from Helpers.signals import *

# Initialising the Signals...
sigs = [[10, 120,0,60],[25, 120,0,60],[48, 120,0,60],[65, 120,0,60],[90, 120,0,60]]
signals = [Signal(sig[0],sig[1],sig[2],sig[3]) for sig in sigs]
positions = [pos[0] for pos in sigs]

# Initialising the Car instance...
car = Car(0, 60, 1)


decellerations = [(5,1), (6,1), (7,1), (15,1), (16,1), (17,1), (22,1), (23,1), (24,1), (25,1), (26,1), (27,1)] # (time, -speed?)

def visualize() : 
    for i in range(signals[-1].pos+ 2): 
        if i == car.pos : 
            print('⧈', end="")
        else : 
            print("|" if i in positions else ".", end="")
    print()

def find_time_req(car : Car, next_sig : Signal) -> int: 
    return round(next_sig.calc_dist(car.pos) / car.speed)

