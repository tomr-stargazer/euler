"""
Largest prime factor
Problem 3
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

http://projecteuler.net/problem=3

"""

from __future__ import division

import numpy as np

def is_prime(value):
    """ Checks if current value is prime. Returns True or False. """

    if value < 2: raise ValueError

    for i in range(2, value):
        if value % i == 0:
            return False

    return True

def primes_up_to(value):
    """ Generates a list of all primes less than or equal to `value`. """

    if value < 2: raise ValueError
    
    primes = []

    for i in range(2, value+1): # the +1 is to include the input value!
        if is_prime(i):
            primes.append(i)

    return primes

def prime_factors_of(value):
    """ Returns all prime factors of `value`. """

    # Okay, so we need to "solve" two problems here:
    # is a given number a factor of `value`?
    #  and
    # is a given number PRIME?

    # I think the simplest non-stupid approach is to generate all primes
    # up to value/2, and then mod them all against `value`.
    # actually, a cute approach would be to start from the top down
    # and just return the first one. we'll see if i need that optimization.
    # (don't optimize prematurely!)

    possible_prime_factors = primes_up_to(value//2)

    prime_factors = []
    
    for i in possible_prime_factors:
        if value % i == 0:
            prime_factors.append(i)

    return prime_factors
    
assert set(prime_factors_of(13195)) == set([5, 7, 13, 29])
assert max(prime_factors_of(13195)) == 29

assert primes_up_to(2) == [2]

print max(prime_factors_of(600851475143))
