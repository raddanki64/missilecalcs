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


def velocity_vs_time(velocity, angle, disp=1, finalvel=[0]):
    if disp == 1:
        out1 = '\n' + oindex + 'Missile velocity vs time plots for ' + repr(angle) + ' degrees'
        print(out1)

        out1 = oindex + 'Time'.ljust(15) \
            + oindex + 'Velocity'.ljust(15)
        print(out1)

    t = time_factor
    while True:
        velocity_z = velocity - 9.81 * t
        if velocity_z > finalvel[0]:
            finalvel[0] = round(velocity_z)
        if velocity_z <= 0:
            break;

        if disp == 1:
            out1 = oindex + repr(t).ljust(15) \
                + oindex + repr(round(velocity_z, 2)).ljust(15)
            print(out1)

        t = t + time_factor


if __name__ == "__main__":
    for langle in launch_angles:
        velocity_vs_time(missile_speed, langle)


