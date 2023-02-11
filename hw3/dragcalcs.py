# given variables
import math
from missilesim import calculate_dynamic_pressure
from accelerationvstime import acceleration_vs_time

mass = 200
diameter = 0.15
missile_speed = 800

pi = 3.14
gravity = 9.81

# computed variables
radius = diameter / 2
surface_area = pi * pow(radius, 2)
weight = mass * gravity

# working variables
time_factor = 20
oindex = ' '.ljust(6)


def calc_thrust(velocity):
    thrust = weight * velocity / gravity
    return thrust


def calc_drag_axial(velocity, angle):
    angle_in_radians = math.radians(angle)
    thrust = calc_thrust(velocity)
    velocity_z = velocity * math.sin(angle_in_radians)

    out1 = '\n' + oindex + 'Missile axial drag vs time plot for' + repr(angle) + ' degrees'
    print(out1)

    out1 = oindex + 'Time'.ljust(15) \
           + oindex + 'Axial drag'.ljust(15)
    print(out1)

    t = time_factor
    while True:
        position_z = velocity_z * t - 0.5 * 9.81 * pow(t, 2)
        if position_z <= 0:
            break;

        dp = calculate_dynamic_pressure(velocity, position_z)
        drag_axial = thrust / (dp * surface_area)

        out1 = oindex + repr(t).ljust(15) \
             + oindex + repr(round(drag_axial, 2)).ljust(15)
        print(out1)

        t = t + time_factor


def calc_drag_induced(velocity, angle):
    angle_in_radians = math.radians(angle)
    normal_force = weight * math.cos(angle_in_radians)
    velocity_z = velocity * math.sin(angle_in_radians)

    out1 = '\n' + oindex + 'Missile induced drag vs time plot for' + repr(angle) + ' degrees'
    print(out1)

    out1 = oindex + 'Time'.ljust(15) \
           + oindex + 'Induced drag'.ljust(15)
    print(out1)

    t = time_factor
    while True:
        position_z = velocity_z * t - 0.5 * 9.81 * pow(t, 2)
        if position_z <= 0:
            break;

        dp = calculate_dynamic_pressure(velocity, position_z)
        drag_induced = normal_force / (dp * surface_area)

        out1 = oindex + repr(t).ljust(15) \
             + oindex + repr(round(drag_induced, 2)).ljust(15)
        print(out1)

        t = t + time_factor


if __name__ == "__main__":
    launch_angle = 40
    accel = [0, 0]

    calc_drag_axial(missile_speed, launch_angle)
    calc_drag_induced(missile_speed, launch_angle)
    acceleration_vs_time(missile_speed, launch_angle, 0, accel)

    out1 = "\n\nAcceleration along y axis (m/s-sq) = " + repr(round(accel[0], 2)).ljust(15)
    print(out1)

    out1 = "Acceleration along z axis (m/s-sq) = " + repr(round(accel[1], 2)).ljust(15)
    print(out1)
