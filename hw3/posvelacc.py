# given variables
from positionvstime import position_vs_time
from velocityvstime import velocity_vs_time

mass = 200
diameter = 0.15
missile_speed = 800

launch_angles = [10, 20, 30, 40, 50, 60]

# computed variables
radius = diameter / 2
surface_area = 3.14 * pow(radius, 2)
weight = mass * 9.81

# working variables
oindex = ' '.ljust(6)

if __name__ == "__main__":
    finalpos = [0]

    out1   = oindex + 'Angle'.ljust(15) \
           + oindex + 'Max Height (km)'.ljust(15)
    print(out1)

    for langle in launch_angles:
        position_vs_time(missile_speed, langle, 0, finalpos)
        out1 = oindex + repr(langle).ljust(15) \
               + oindex + repr(finalpos[0]).ljust(15)
        print(out1)

    out1 = '\n\n' + oindex + 'Angle'.ljust(15) \
         + oindex + 'Max Velocity (m/s)'.ljust(15)
    print(out1)

    finalvel = [0]
    for langle in launch_angles:
        velocity_vs_time(missile_speed, langle, 0, finalvel)
        out1 = oindex + repr(langle).ljust(15) \
               + oindex + repr(finalvel[0]).ljust(15)
        print(out1)
