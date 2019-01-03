#!/bin/env python3

from math import sin, cos, tau

# positin of the 10k witche (x, y)
pos = [132.4, 112]

# distance to switch center 
radius = 10

# angular position of first resistor
start_angle = 255

for r in range(12):
    # rotation of the part
    angle = r * 30
    # new position of the part
    positional_angle = start_angle - angle
    rads = (positional_angle / 360) * tau
    pos_x = round(pos[0] + cos(rads) * radius, 1)
    pos_y = round(pos[1] - sin(rads) * radius, 1)
    print(f"MOVE {r} TO ({pos_x}, {pos_y})")