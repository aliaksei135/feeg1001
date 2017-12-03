import math

import matplotlib.pyplot as pp
from scipy.optimize import brentq


def f1(x):
    """accepts an number x as input and computes and returns"""
    return math.cos(2 * math.pi * x) * math.exp(-1 * x ** 2)


def f2(x):
    """accepts the number x as input and computes and returns"""
    return math.log(x + 2.2)


def positive_places(f, xs):
    """takes as arguments some function f and a list of numbers xs and returns
     a list of those-and-only-those elements x of xs for which f(x)
     is strictly greater than zero"""
    return [f(x) for x in xs if f(x) > 0]


def create_plot_data(f, xmin, xmax, n):
    """ returns a tuple (xs, ys) where xs and ys are two sequences,
    each containing n numbers"""
    xs = []
    ys = []
    for i in range(0, n):
        a = xmin + (i * ((xmax - xmin) / (n - 1)))
        xs.append(a)
        ys.append(f(a))
    return (xs, ys)


def myplot():
    """computes f1(x) [by calling create_plot_data] and plots f1(x) using
    1001 points for x from -2 to +2. The function should return None"""
    f1plot = create_plot_data(f1, -2, 2, 1001)
    f2plot = create_plot_data(f2, -2, 2, 1001)
    pp.plot(f1plot[0], f1plot[1], label='f1')
    pp.plot(f2plot[0], f2plot[1], label='f2')
    pp.xlabel('xs')
    pp.grid()
    pp.legend()
    pp.savefig('plot.pdf')
    pp.savefig('plot.png')
    return None


def find_cross():
    """find the value x (approximately) for which f1(x) = cos(2 * pi * x)
    * exp(-x * x) and f2(x) = log(x + 2.2) have the same value. We are only
    interested in the solution where x > 0."""
    return brentq((lambda x: f1(x) - f2(x)), 0, 0.15)


def reverse_dic(d):
    """takes a dictionary d as the input argument and returns a dictionary r.
    If the dictionary d has a key k and an associated value v, then the
    dictionary r should have a key v and a value k"""
    # if len(d) == 0:
    #     return {}
    # return dict([(v, k) for k, v in d.iteritems()])
    return dict(zip(d.values(), d.keys()))
