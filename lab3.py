import math


def degree(x):
    """takes an argument x in radian and returns the corresponding value in degrees"""
    return (x*360)/(2*math.pi)


def min_max(xs):
    """computes the minimum value xmin of the elements in the list xs,
     and the maximum value xmax of the elements in the list, and returns a tuple (xmin,xmax)"""
    return min(xs), max(xs)


def geometric_mean(xs):
    """returns the geometric mean of the numbers given in the list xs."""
    p = 1
    for n in xs:
        p = p*n
    return p**0.5


def swing_time(l):
    """returns the time T [in seconds] needed for an idealized pendulum
    of length L [in meters] to complete a single oscillation"""
    return (2*math.pi)*((l/9.81)**0.5)


def range_squared(n):
    """takes an non-negative integer value n and that returns the list [0, 1, 4, 9, 16, 25, ..., (n-1)^2"""
    if n == 0:
        return []
    l = []
    for n in range(0, n):
        l.append(n**2)
    return l


def count(element, seq):
    """counts how often the given element element occurs in the given sequence seq, and returns this integer value"""
    count = 0
    for e in seq:
        if e == element:
            count += 1
    return count
