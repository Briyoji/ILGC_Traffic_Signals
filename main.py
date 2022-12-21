from Helpers.helpers import *

visualize()
while car.pos <= signals[-1].pos +2 : 
    car.update_pos()
    visualize()