import math
from missilesim import calculate_density

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


def acceleration_vs_time(velocity, angle, disp=1, accel=[0,0]):
    if disp == 1:
        out1 = '\n' + oindex + 'Missile acceleration vs time plots for ' + repr(angle) + ' degrees'
        print(out1)

        out1 = oindex + 'Time'.ljust(15) \
             + oindex + 'Acceleration-Y'.ljust(15) \
             + oindex + 'Acceleration-Z'.ljust(15)
        print(out1)

    angle_in_radians = math.radians(angle)

    t = time_factor
    while True:
        velocity_z = velocity - 9.81 * t
        if velocity_z <= 0:
            accel[0] = acceleration_y
            accel[1] = acceleration_z
            break;

        position_z = velocity_z * t - 0.5 * 9.81 * pow(t, 2)
        density = calculate_density(position_z)
        drag = (4.7 * density * velocity * velocity * surface_area) / 2;

        acceleration_y = ((drag * math.sin(angle_in_radians) + weight) / mass)
        acceleration_z = ((drag * math.cos(angle_in_radians)) / mass)

        if disp == 1:
            out1 = oindex + repr(t).ljust(15) \
                 + oindex + repr(round(acceleration_y, 2)).ljust(15) \
                 + oindex + repr(round(acceleration_z, 2)).ljust(15)
            print(out1)

        t = t + time_factor


if __name__ == "__main__":
    for langle in launch_angles:
        acceleration_vs_time(missile_speed, langle)
