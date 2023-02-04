import math
from missilesim import calculate_density

# given variables
launch_angles = [10, 20, 30, 40, 50, 60, 70, 80]
missile_speed = 600
surface_area = 0.1
mass = 10

# computed variables
weight = mass * 9.81

# working variables
time_factor = 4
oindex = ' '.ljust(6)


def acceleration_vs_time(velocity, angle):
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
            break;

        position_z = velocity_z * t - 0.5 * 9.81 * pow(t, 2)
        density = calculate_density(position_z)
        drag = (4.7 * density * velocity * velocity * surface_area) / 2;

        acceleration_y = ((drag * math.sin(angle_in_radians) + weight) / mass)
        acceleration_z = ((drag * math.cos(angle_in_radians)) / mass)

        out1 = oindex + repr(t).ljust(15) \
               + oindex + repr(round(acceleration_y, 2)).ljust(15) \
               + oindex + repr(round(acceleration_z, 2)).ljust(15)

        print(out1)

        t = t + time_factor


def velocity_vs_time(velocity, angle):
    out1 = '\n' + oindex + 'Missile velocity vs time plots for ' + repr(angle) + ' degrees'
    print(out1)

    out1 = oindex + 'Time'.ljust(15) \
           + oindex + 'Velocity'.ljust(15)
    print(out1)

    t = time_factor
    while True:
        velocity_z = velocity - 9.81 * t
        if velocity_z <= 0:
            break;

        out1 = oindex + repr(t).ljust(15) \
               + oindex + repr(round(velocity_z, 2)).ljust(15)

        print(out1)

        t = t + time_factor


def position_vs_time(velocity, angle):
    angle_in_radians = math.radians(angle)
    velocity_y = velocity * math.cos(angle_in_radians)
    velocity_z = velocity * math.sin(angle_in_radians)

    out1 = '\n' + oindex + 'Missile position vs time plots for ' + repr(angle) + ' degrees'
    print(out1)

    out1 = oindex + 'Time'.ljust(15) \
           + oindex + 'Y'.ljust(15) \
           + oindex + 'Z'.ljust(15) \
           + oindex + 'Y+Z'.ljust(15)
    print(out1)

    t = time_factor
    while True:
        position_y = velocity_y * t
        position_z = velocity_z * t - 0.5 * 9.81 * pow(t, 2)
        if position_z <= 0:
            break;

        position_sum = position_y + position_z

        out1 = oindex + repr(t).ljust(15) \
               + oindex + repr(round(position_y, 2)).ljust(15) \
               + oindex + repr(round(position_z, 2)).ljust(15) \
               + oindex + repr(round(position_sum, 2)).ljust(15)

        print(out1)

        t = t + time_factor


if __name__ == "__main__":
    for langle in launch_angles:
        position_vs_time(missile_speed, langle)

    for langle in launch_angles:
        velocity_vs_time(missile_speed, langle)

    for langle in launch_angles:
        acceleration_vs_time(missile_speed, langle)
