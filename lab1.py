def average(a, b):
    """Given parameters a and b, compute and
       return the arithmetic mean of a and b"""
    return (a + b) * 0.5


def distance(a, b):
    """returns the distance between numbers a and b"""
    return abs(a - b)


def geometric_mean(a, b):
    """returns the geometric mean of two numbers"""
    return (a * b) ** 0.5


def pyramid_volume(A, h):
    """returns the volume of a pyramid with base area A and height h"""
    return (A * h) / 3
