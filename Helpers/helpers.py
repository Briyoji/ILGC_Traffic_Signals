from car import *
from signals import *

sigs = [[10, 120,5,60],[25, 120,5,60],[48, 120,5,60],[65, 120,5,60],[90, 120,5,60]]
signals = []
positions = [pos[0] for pos in sigs]

car = Car(0, 60, 1)

for sig in sigs :
    signals.append(Signal(sig[0],sig[1],sig[2],sig[3]))

for i in range(signals[-1].pos+ 2): 
    print("|" if i in positions else ".", end="")

print()