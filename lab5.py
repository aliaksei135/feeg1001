import re

import numpy as np


def count_sub_in_file(filename, s):
    """ return the number of occurrences of s
    in the file given through filename"""
    try:
        with open(filename, 'rt') as f:
            text = f.read()
            o = text.count(s)
            f.close()
            return o
    except FileNotFoundError or FileExistsError as e:
        return -1


def count_vowels(s):
    """returns the number of letters 'a', 'e', 'i', 'o', 'u',
     'A', 'E', 'I', 'O', 'U' in a given string s
     (the return value is of type integer)"""
    v = re.findall('[aeiou]', s, flags=re.IGNORECASE)
    return len(v)


def vector_product3(a, b):
    """ return a list which contains the vector
    product of 3d-vectors a and b"""
    a = np.array(a)
    b = np.array(b)
    return list(np.cross(a, b))


def seq_mult_scalar(a, s):
    """takes a list of numbers a and a scalar (i.e. a number) s.
    For the input a=[a0, a1, a2,.., an]
    the function should return [s * a0, s * a1, s * a2, ..., s * an]"""
    a = np.array(a)
    return list(a * s)


def powers(n, k):
    """returns the list [1,n,n^2,n^3,...,n^k] where k is an integer."""
    a = []
    j = 0
    for i in range(1, k + 2):
        a.append(n ** j)
        j += 1
        if j == k + 1:
            break
    return a


def traffic_light(load):
    """return the string:
    "green" for values of load below 0.7.
    "amber" for values of load equal to or
    greater than 0.7 but smaller than 0.9
    "red" for values of load equal to 0.9 or greater than 0.9
    """
    if load < 0.7:
        return 'green'
    elif load >= 0.7 and load < 0.9:
        return 'amber'
    elif load >= 0.9:
        return 'red'
