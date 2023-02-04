import math

def calculate_temp(height):
    if height > 25000:
        temp = -131.21 + .00299 * height
    elif height < 11000:
            temp = 15.04 - .00649 * height
    else:
        temp = -56.46

    return temp

def calculate_pressure(height):
    temp = calculate_temp(height)
    if height > 25000:
        temp_k = (temp + 273.1) / 216.6
        pressure = 2.488 * pow(temp_k, -11.388)
    elif height < 11000:
        temp_k = (temp + 273.1) / 288.08
        pressure = 101.29 * pow(temp_k, 5.256)
    else:
        x1 = 1.73 - .000157 * height
        pressure = 22.65 * pow(math.e, x1)

    return pressure

def calculate_density(height):
    temp = calculate_temp(height)
    pressure = calculate_pressure(height)
    temp_k = (temp + 273.1)
    density = pressure / (.2869 * temp_k)
    return density

def calculate_dynamic_pressure(velocity, height):
    density = calculate_density(height)
    dynamic_pressure = (density * velocity * velocity) / 2
    return dynamic_pressure

def calculate_mac(velocity, height):
    mach = 4
    return mach


if __name__ == "__main__":
    print("Missile simulator\n")
    print("Enter height: ")
    input_h = input()

    print("Enter velocity: ")
    input_v = input()

    mheight = int(input_h)
    mvelocity = int(input_v)

    ctemp = calculate_temp(mheight)
    cpres = calculate_pressure(mheight)
    cdens = calculate_density(mheight)
    cpressure = calculate_dynamic_pressure(mvelocity, mheight)
    cmach = calculate_mac(mvelocity, mheight)

    print("\n\nComputed values")
    out1 = 'Height = ' + repr(mheight) \
         + ', Temperature = ' + repr(ctemp) \
        + ', Pressure = ' + repr(cpres) \
        + ', Density = ' + repr(cdens)
    print(out1)

    out1 = 'Velocity - ' + repr(mvelocity) \
        + ', Dynamic pressure = ' + repr(cpressure) \
        + ', Mach = ' + repr(cmach)
    print(out1)
