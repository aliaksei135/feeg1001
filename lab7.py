def count_chars(s):
    """takes a string s and returns a dictionary.
    The dictionarys keys are the set of characters that occur in string s."""
    letters = {}
    for l in s:
        if l in letters.keys():
            letters[l] += 1
        else:
            letters[l] = 1
    return letters


def derivative(f, x, eps=1e-6):
    """computes a numerical approximation of the first derivative
    of the function f(x) using central differences and returns it"""
    return (f(x + (eps / 2)) - f(x - (eps / 2))) / eps


def newton(f, x, feps, maxit):
    """takes a function f(x) and an initial guess x for the root of the
    function f(x), an allowed tolerance feps and the maximum number
    of iterations that are allowed maxit. Returns result x"""
    iters = 0
    while abs(f(x)) > feps:
        if iters > maxit:
            raise RuntimeError('Failed after %d iterations' % maxit)
        x = x - f(x) / derivative(f, x)
        iters += 1
    return x


def is_palindrome(s):
    """takes a string s and returns the value True if s is a palindrome
     and returns False otherwise"""
    if len(s) < 2:
        return True
    else:
        return s == s[::-1]
