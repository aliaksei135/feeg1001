# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 13:22:39 2017

@author: ap9g17
"""


def box_volume(a, b, c):
    """calculates and returns the volume of a cuboid
    with edge lengths a, b, c."""
    return a * b * c


def fall_time(h):
    """returns the time (in seconds) needed for an object falling
    from a tower of height h (in meters)
    to hit the ground (ignoring air friction)"""
    return ((2 * h) / 9.81) ** 0.5


def interval_point(a, b, x):
    """interprets a and b as the start and end point and x as a fraction that
    determines how far to go towards b, starting at a and returns the result"""
    return a + ((b - a) * x)


def impact_velocity(h):
    """returns the velocity (in metre per second) with which an object
    falling from a height of h meters will hit the ground"""
    return fall_time(h) * 9.81


def signum(x):
    """returns 1 if x > 0
        returns 0 if x = 0
        returns -1 if x < 0"""
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0


def seconds2days(n):
    """accepts a number of seconds and converts the number of
    seconds in the corresponding number of days"""
    return n / 86400


def box_surface(a, b, c):
    """computes and returns the surface area of a box (i.e. cuboid)
    with these edge lengths a, b, and c."""
    return 2 * ((a * b) + (b * c) + (a * c))


def triangle_area(a, b, c):
    """ computes and returns the area A of a triangle
    with edge lengths a, b, and c"""
    s = (a + b + c) / 2
    return (s * (s - a) * (s - b) * (s - c)) ** 0.5
