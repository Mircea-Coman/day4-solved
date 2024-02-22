"""
A collection of simple math operations
"""

def simple_add(a,b):
    """
    simple_add(a, b)
    The sum of two numbers

    Parameters
    ----------
    a : float
        First summand
    b : float
        Second summand

    Returns
    -------
    float
    Sum of a and b

    See Also
    --------
    simple_sub : Subtraction
    """
    return a+b

def simple_sub(a,b):
    """
    simple_sub(a, b)
    The difference of two numbers

    Parameters
    ----------
    a :
        The minuend
    b :
        The subtrahend

    Returns
    -------
    Difference of a and b

    See Also
    --------
    simple_add : Addition
    """
    return a-b

def simple_mult(a,b):
    """
    simple_mult(a, b)
    The product of two numbers

    Parameters
    ----------
    a :
        The first factor
    b :
        The second factor

    Returns
    -------
    Product of a and b

    See Also
    --------
    simple_div : Division
    """
    return a*b

def simple_div(a,b):
    """
    simple_div(a, b)
    The ratio of two numbers

    Parameters
    ----------
    a :
        The divident
    b :
        The divisor

    Returns
    -------
    Ratio of a and b

    See Also
    --------
    simple_mult : Multiplication
    """
    return a/b

def poly_first(x, a0, a1):
    """
    poly_first(x, a0, a1)
    The result of a first order polynomial

    Parameters
    ----------
    x :
        The argument of the polynomial function
    a0 :
        Coefficient of the constant term
    a1 :
        Coefficient of the linear term

    Returns
    -------
    The value of the linear polynomial, with coefficient a0 and a1 evaluated at x

    See Also
    --------
    poly_second : Quadratic Polynomial
    """
    return a0 + a1*x

def poly_second(x, a0, a1, a2):
    """
    poly_second(x, a0, a1, a2)
    The result of a second order polynomial

    Parameters
    ----------
    x :
        The argument of the polynomial function
    a0 :
        Coefficient of the constant term
    a1 :
        Coefficient of the linear term
    a2 :
        Coefficient of the quadratic term

    Returns
    -------
    The value of the quadratic polynomial, with coefficient a0, a1 and a2 evaluated at x

    See Also
    --------
    poly_first : Linear Polynomial
    """

    return poly_first(x, a0, a1) + a2*(x**2)

# Feel free to expand this list with more interesting mathematical operations...
# .....
