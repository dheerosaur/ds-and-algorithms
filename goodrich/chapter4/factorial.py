
def factorial(n):
    """
    Returns the factorial of n that is defined as 1 for 1
    and the product of all numbers till N (including N) for N
    >>> factorial(0)
    1

    >>> factorial(5)
    120

    >>> factorial(10)
    3628800
    """
    if n == 0:
        return 1
    return n * factorial(n - 1)
