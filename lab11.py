import math

import numpy as np
import scipy.integrate
import scipy.optimize


def f(x):
    """Computes and returns a set function"""
    try:
        return ((math.exp(-x ** 2)) / (1 + x ** 2)) \
               + ((2 * math.cos(x) ** 2) / (1 + (x - 4) ** 2))
    except TypeError:
        return [((math.exp(-n ** 2)) / (1 + n ** 2))
                + ((2 * math.cos(n) ** 2) / (1 + (n - 4) ** 2)) for n in x]


def make_multiplier(factor):
    """ returns a function which takes an argument x
    and which should return factor * x"""
    return lambda x: x * factor


def solve_freefall(ts, v0, m=80, A=0.5, g=9.81, c=0.25):
    """computes and returns the numerical
    solution of the differential equation"""

    def rhs(v, t):
        return g - ((A * c * v ** 2) / (m))

    return scipy.integrate.odeint(rhs, v0, ts)


def integrate_f_from0(b):
    """The function integrate_f_from0(b)
    should return a floating point number."""
    return scipy.integrate.quad(f, 0, b)[0]


def find_max_f():
    """returns (an approximation of) the x for
    which f(x) takes the maximum value."""
    return scipy.optimize.fmin(lambda x: -f(x), 4)[0]


def find_f_equals_1():
    """returns a float which is (an approximation of) the x
    for which f(x)=1. We are only interested
    in the solution where x is negative."""
    return scipy.optimize.fsolve(lambda x: np.asarray(f(x)) - 1, 1)


def lin_int(xs, ys):
    """returns a callable object f(x) which returns y(x) using
    linear interpolation between the points provided by
    the data xs and ys."""
    return lambda x: np.interp(x, xs, ys)


def make_oscillator(frequency):
    """ returns a function which takes a floating point value t
    to represent time, and returns sin(t * frequency)"""
    return lambda x: math.sin(x * frequency)
