import math

import numpy as np
import scipy.optimize
from matplotlib import pylab


def model(t, Ti, Ta, c):
    """should return a single value if t is a floating point number
    and an array if t is an array."""
    try:
        return [((Ti - Ta) * math.exp(-n / c) + Ta) for n in t]
    except TypeError:
        return (Ti - Ta) * math.exp(-t / c) + Ta


def read2coldata(filename):
    """function should return a tuple of two numpy-arrays where the first
    contains all the data from the first column in the file, and the second
    all the data in the second column."""
    x, y = [], []
    with open(filename, 'rt') as f:
        for line in f:
            tokens = line.split()
            x.append(float(tokens[0]))
            y.append(float(tokens[1]))
        f.close()
        print(type(x))
    return (np.asarray(x), np.asarray(y))


def extract_parameters(ts, Ts):
    """estimate and return a tuple of the model parameters Ti, Ta and c"""
    popt, pcov = scipy.optimize.curve_fit(model, ts, Ts, p0=[100, 20, 400])
    return tuple(popt)


def plot(ts, Ts, Ti, Ta, c):
    """Input Parameters:

      ts : Data for time (ts)
                (numpy array)
      Ts : data for temperature (Ts)
                (numpy arrays)
      Ti : model parameter Ti for Initial Temperature
                (number)
      Ta : model parameter Ta for Ambient Temperature
                (number)
      c  : model parameter c for the time constant
                (number)

    This function will create plot that shows the model fit together
    with the data.

    Function returns None.
    """

    pylab.plot(ts, Ts, 'o', label='data')
    fTs = model(ts, Ti, Ta, c)
    pylab.plot(ts, fTs, label='fitted')
    pylab.legend()
    pylab.show()


def sixty_degree_time(Ti, Ta, c):
    """return an estimate of the number of seconds after which the temperature
    of the drink has cooled down to 60 degree Celsius"""
    return scipy.optimize.fsolve(lambda x:
                                 np.asarray(model(x, Ti, Ta, c)) - 60, 300)
