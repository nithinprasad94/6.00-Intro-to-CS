# 6.00 Problem Set 2
#
# Successive Approximation
#

def evaluate_poly(poly, x):
    """
    Computes the polynomial function for a given value x. Returns that value.

    Example:
    >>> poly = (0.0, 0.0, 5.0, 9.3, 7.0)    # f(x) = 7x^4 + 9.3x^3 + 5x^2
    >>> x = -13
    >>> print evaluate_poly(poly, x)  # f(-13) = 7(-13)^4 + 9.3(-13)^3 + 5(-13)^2
    180339.9

    poly: tuple of numbers, length > 0; poly[0] is coeff for x^0, poly[1] is coeff
    of x^1, etc
    x: number
    returns: float
    """

    #Store powers to the x corresponding to each coefficient
    powers_list = range(len(poly))
    #print powers_list
    #print poly

    sum_list = [poly[i]*x**powers_list[i] for i in range(len(poly))]
    #print sum_list
    final_val = sum(sum_list)

    return final_val


def compute_deriv(poly):
    """
    Computes and returns the derivative of a polynomial function. If the
    derivative is 0, returns (0.0,).

    Example:
    >>> poly = (-13.39, 0.0, 17.5, 3.0, 1.0)    # x^4 + 3x^3 + 17.5x^2 - 13.39
    >>> print compute_deriv(poly)        # 4x^3 + 9x^2 + 35^x
    (0.0, 35.0, 9.0, 4.0)

    poly: tuple of numbers, length > 0
    returns: tuple of numbers
    """

    deriv_list = []
    powers_list = range(len(poly))

    for i in range(len(poly)):
        if (i == 0):
            #Do nothing for the constant term (shrinks list by 1)
            pass
        else:
            coeff = poly[i]*(powers_list[i])
            deriv_list.append(coeff)

    deriv_tuple = tuple(deriv_list)

    return deriv_tuple

def compute_root(poly, x_0, epsilon):
    """
    Uses Newton's method to find and return a root of a polynomial function.
    Returns a tuple containing the root and the number of iterations required
    to get to the root.

    Example:
    >>> poly = (-13.39, 0.0, 17.5, 3.0, 1.0)    #x^4 + 3x^3 + 17.5x^2 - 13.39
    >>> x_0 = 0.1
    >>> epsilon = .0001
    >>> print compute_root(poly, x_0, epsilon)
    (0.80679075379635201, 8.0)

    poly: tuple of numbers, length > 1.
         Represents a polynomial function containing at least one real root.
         The derivative of this polynomial function at x_0 is not 0.
    x_0: float
    epsilon: float > 0
    returns: tuple (float, int)
    """
    #Compute f(x0)
    poly_val = evaluate_poly(poly,x_0)

    #Base Case:
    if (abs(poly_val) < epsilon):
        return (x_0,1)

    #Recursive Case:
    else:
        x_1 = x_0 - (poly_val*1.0)/evaluate_poly((compute_deriv(poly)),x_0)
        (root,iterations) = compute_root(poly,x_1,epsilon)
        return (root,iterations+1)


