import numpy as np
import scipy
import scipy.integrate
import scipy.stats
import sympy
from sympy.abc import x

"""Some support functions"""


def code0():
    """A trivial code - no change."""
    return {}


def code1():
    """A very simple example (symmetric)."""
    return {'e': 'x', 'x': 'e'}


def code2():
    """A simple example i->s, s->g and g->i."""
    return {'i': 's', 's': 'g', 'g': 'i'}


def code3():
    """A more complicated code."""
    dic = {}
    # lower case letters
    dic['z'] = 'a'
    for i in range(ord('a'), ord('z')):
        dic[chr(i)] = chr(i + 1)
    # upper case letters
    dic['Z'] = 'A'
    for i in range(ord('A'), ord('Z')):
        dic[chr(i)] = chr(i + 1)
    # space, stop and some other special characters
    dic[' '] = '$'
    dic['.'] = '#'
    dic['#'] = '.'
    dic['$'] = ' '
    dic['?'] = '!'
    dic['!'] = '?'
    return dic


def check_code_is_reversible(dic):
    """Given a dictionary used as a code mapping, this function checks
    whether the set of keys is the same set of values: if the elements
    in the keys are the same unique set as those in the values, then
    this mapping is bijective (the set of values is then actually a
    permutation of the set of input values) and can be inverted.

    If this is not the case, some debug information is printed, and a
    ValueError exception raised.
    """

    unique_keys = set()
    unique_vals = set()
    for key, val in dic.items():
        unique_keys.add(key)
        unique_vals.add(val)
    if unique_vals != unique_keys:
        print("Code is not reversible:")
        print("keys are   %s", sorted(unique_keys))
        print("values are %s", sorted(unique_vals))
        raise ValueError("Code is not reversible - stopping here")
    return True


def test_codes():
    """Check that codes defined above are reversible."""
    for c in (code0(), code1(), code2(), code3()):
        assert check_code_is_reversible(c)


secretmessage = \
    "Zpv$ibwf$tvddfttgvmmz$efdpefe$uijt$tfdsfu$nfttbhf#$Dpohsbuvmbujpot?"


# if this file is executed on it's own, check codes given
# if __name__ == "__main__":
#     test_codes()


################################################################

def trapez(f, a, b, n):
    """The function should use the composite trapezoidal rule to compute A
    and return this value."""
    x = np.linspace(a, b, n + 1)
    print(x)
    y = []
    for p in x:
        y.append(f(p))
    return np.trapz(y, x)


def encode(code, msg):
    """The function should apply the mapping to each character of the string
    as described above and return the encoded output string."""
    result = ""
    keys = code.keys()
    for l in msg:
        if l in keys:
            result += code[l]
        else:
            result += l
    return result


def reverse_dic(d):
    """takes a dictionary d as the input argument and returns a dictionary r.
    If the dictionary d has a key k and an associated value v, then the
    dictionary r should have a key v and a value k"""
    return dict(zip(d.values(), d.keys()))


def finderror(n):
    """The function should compute the integral of f(x) = x*x with
    integration limits a = -1 and b = 2 numerically. The function should then
    subtract this numerical result A from the exact integral value I
    and return the difference."""
    approx = trapez(lambda x: x * x, -1, 2, n)
    act = sympy.integrate(x ** 2, (x, -1, 2))
    return act - approx


def using_quad():
    """computes the integral of x2 from a=-1 to b=2 using function quad from
    scipy.integrate. The function using_quad should return the value that
    the quad() function returns"""
    return scipy.integrate.quad(lambda x: x ** 2, -1, 2)


def std_dev(x):
    """takes a list x of floating point numbers, and computes and returns the
    corrected sample standard deviation of the floating point numbers
    in the list x"""
    return np.std(x, ddof=1)


def decode(code, encoded_msg):
    """takes a dictionary code that contains the mapping dictionary with which
    the string encoded_msg has been encoded. The function decode should
    return the decoded message."""
    result = ""
    codedict = reverse_dic(code)
    keys = codedict.keys()
    for l in encoded_msg:
        if l in keys:
            result += codedict[l]
        else:
            result += l
    return result
