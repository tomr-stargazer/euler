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

# first: go through a bunch of numbers. Everytime you hit a divisor:
#  decimate evilnumber by that value (as many times as is possible) 
#  and then keep going til you've found all the factors 
#  (i.e. the decimated number hits one) or you've checked 
#  every factor up to sqrt(evilnumber).
#  Then you're left with two numbers: the most recent divisor that worked,
#  and the decimated number that remained. 
#  They're both prime factors - return the larger of the two.
#   (sometimes one of those two is actually 1, 
#    in which case your input was prime and you're golden.)
#   (this actually works as a pretty neat prime checker, too!)

def find_largest_prime_factor(value):
    """ Finds the largest prime factor of a given number. """
    # I think it really works! and is somewhat optimal!
    
    current_largest_factor = 1
    n = 2

    current_value = value

    while n <= np.sqrt(value) and current_value > 1:

        while current_value % n == 0:

            current_value = current_value//n
            current_largest_factor = n
            
        n += 1

    return max(current_largest_factor, current_value)

assert find_largest_prime_factor(13195) == 29

print find_largest_prime_factor(600851475143)

        
