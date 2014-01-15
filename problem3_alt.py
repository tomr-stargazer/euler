"""
Largest prime factor
Problem 3
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

http://projecteuler.net/problem=3

"""

from __future__ import division

import numpy as np

# THIS APPROACH WILL BE DIFFERENT.
# We'll take the big evil number 600851475143

# and hack it down piece by piece.

# first: go through a bunch 
# If so, decimate evilnumber by that value (as many times as is possible) 
#        and move onto the next iteratively-generated prime.

def find_largest_prime_factor(value):
    """ Finds the largest prime factor of a given number. """

    current_largest_factor = 2
    n = 2

    current_value = value

    while n < np.sqrt(value):

        if current_value % n == 0:

            current_value = current_value/n
            current_largest_factor = n
            
        n += 1

    return current_largest_factor

assert find_largest_prime_factor(13195) == 29

print find_largest_prime_factor(600851475143)

        
