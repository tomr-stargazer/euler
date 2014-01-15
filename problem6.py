"""
Sum square difference
Problem 6
The sum of the squares of the first ten natural numbers is,

1**2 + 2**2 + ... + 10**2 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)**2 = 55**2 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

http://projecteuler.net/problem=6

"""

import numpy as np

def sum_of_squares_up_to(value):
    """ Computes the sum of squares up to the input value. """

    return np.sum(np.arange(value+1)**2)

def square_of_sum_up_to(value):
    """ Computes the square of the sum of all values up to the input. """

    return np.sum(np.arange(value+1))**2
    

def diff_sumofsquares_squareofsum_up_to(value):

    return np.abs(sum_of_squares_up_to(value) - square_of_sum_up_to(value))

assert sum_of_squares_up_to(10) == 385
assert square_of_sum_up_to(10) == 3025
assert diff_sumofsquares_squareofsum_up_to(10) == 2640

print diff_sumofsquares_squareofsum_up_to(100)
