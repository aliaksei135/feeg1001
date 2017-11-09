def positive_places(f, xs):
    """takes as arguments some function f and a list of numbers xs
     and returns a list of those-and-only-those elements x of xs
     for which f(x) is strictly greater than zero"""
    l = []
    for n in xs:
        if f(n) > 0:
            l.append(n)
    return l


def eval_f_0123(f):
    """evaluates the function f=f(x) at positions x=0, x=1, x=2 and x=3.
     The function should return the list [f(0), f(1), f(2), f(3)]."""
    return [f(n) for n in range(0, 4)]


def eval_f(f, xs):
    """takes a function f = f(x) and a list xs of values that should be
     used as arguments for f. The function eval_f should apply the function f
    subsequently to every value x in xs, and return a list fs of function
    values. I.e. for an input argument xs=[x0, x1, x2,..., xn] the function
    eval_f(f, xs) should return [f(x0), f(x1), f(x2), ..., f(xn)]."""
    fs = []
    for x in xs:
        fs.append(f(x))
    return fs


def sum_f(f, xs):
    """returns the sum of the function values of f evaluated
    at values x0, x1, x2, ..., xn where xs=[x0,x1,x2,...,xn]."""
    return sum(eval_f(f, xs))


def box_volume_UPS(a=13, b=11, c=2):
    """returns the volume of a box with edge lengths a, b and c.
    Inputs should be provided in inch, and the output
     should be expressed in inch^3."""
    return a * b * c
