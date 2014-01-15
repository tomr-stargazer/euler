"""
Multiples of 3 and 5
Problem 1
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

http://projecteuler.net/problem=1

"""

from __future__ import division

import numpy as np

def sum_multiples_of_3_or_5_below_value(max_value):
    """
    Solves the above problem for any "max value".

    """

    multiples = []

    for i in range(max_value):

        if (i % 3) == 0 or (i % 5) == 0:
            multiples.append(i)
            
    return np.sum(multiples)

# Let's use the initial hint as a unit test.
assert sum_multiples_of_3_or_5_below_value(10) == 23

print sum_multiples_of_3_or_5_below_value(1000)
