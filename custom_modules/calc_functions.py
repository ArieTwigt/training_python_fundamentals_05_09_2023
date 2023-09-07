import math


def calc_size_circle(diameter):
    radius = diameter / 2
    size = math.pow(radius, 2) * math.pi
    return size


def calc_pythagoras(a, b):
    c_2 = math.pow(a, 2) + math.pow(b, 2)
    c = math.sqrt(c_2)
    return c
