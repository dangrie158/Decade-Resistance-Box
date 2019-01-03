#!/bin/env python3

from math import sin, cos, tau

# 1/8 the board width (used to calculate the switch positions)
s_x = 13.125

# positin of the switches (x, y)
switch_positions = {
    '1Ω': (s_x*7, 26),
    '10Ω': (s_x*5, 26),
    '100Ω': (s_x*3, 26),
    '1kΩ': (s_x*1, 26),
    '10kΩ': (s_x*6, 51),
    '100kΩ': (s_x*4, 51),
    '1MΩ': (s_x*2, 51),
}

# distance to switch center 
radius = 8.5
# angular position of first resistor
start_angle = 270

for sw_num, switch in enumerate(switch_positions.items()):
    name, pos = switch
    # new position for the switch
    print(f"MOVE '{name}' ({pos[0]} {pos[1]})")
    print(f"MOVE '{name}>NAME' ({pos[0]} {pos[1]})")
    print(f"CHANGE ALIGN 'center' ({pos[0]} {pos[1]})")
    for r in range(1, 11):
        # name of the part to position
        r_name = f"R{10 * sw_num + r}"
        # rotation of the part
        angle = r * 30
        # new position of the part
        positional_angle = start_angle - angle
        rads = (positional_angle / 360) * tau
        pos_x = pos[0] + cos(rads) * radius
        pos_y = pos[1] + sin(rads) * radius
        print(f"MOVE '{r_name}' ({pos_x} {pos_y})")
        print(f"ROTATE =MR{angle} '{r_name}'")

        # new position of the partname
        name_pos_x = pos[0] + cos(rads) * (radius * 1.15)
        name_pos_y = pos[1] + sin(rads) * (radius * 1.15)
        print(f"MOVE '{r_name}>NAME' ({name_pos_x} {name_pos_y})")
        print(f"CHANGE ALIGN 'center-right' ({name_pos_x} {name_pos_y})")
        print(f"CHANGE FONT 'vector' ({name_pos_x} {name_pos_y})")
        print(f"ROTATE =MR{angle + 90} '{r_name}>NAME'")

        #delete the value text of the part
        #print(f"DELETE '{r_name}>VALUE'")
