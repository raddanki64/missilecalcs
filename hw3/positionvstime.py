import math

# given variables
mass = 200
diameter = 0.15
missile_speed = 800

launch_angles = [10, 20, 30, 40, 50, 60]

# computed variables
radius = diameter / 2
surface_area = 3.14 * pow(radius, 2)
weight = mass * 9.81

# working variables
time_factor = 4
oindex = ' '.ljust(6)


def position_vs_time(velocity, angle, disp=1, finalpos=[0]):
    angle_in_radians = math.radians(angle)
    velocity_y = velocity * math.cos(angle_in_radians)
    velocity_z = velocity * math.sin(angle_in_radians)

    if disp == 1:
        out1 = '\n' + oindex + 'Missile position vs time plots for ' + repr(angle) + ' degrees'
        print(out1)

        out1 = oindex + 'Time'.ljust(15) \
             + oindex + 'Position (km)'.ljust(15)
        print(out1)

    t = time_factor
    while True:
        position_y = velocity_y * t
        position_z = velocity_z * t - 0.5 * 9.81 * pow(t, 2)
        if position_z <= 0:
            finalpos[0] = round(position_y / 1000)
            break;

        position_sum = position_y + position_z
        position_sum = position_sum / 1000

        if disp == 1:
            out1 = oindex + repr(t).ljust(15) \
                 + oindex + repr(round(position_sum, 2)).ljust(15)
            print(out1)

        t = t + time_factor


if __name__ == "__main__":
    for langle in launch_angles:
        position_vs_time(missile_speed, langle)

