"""
Largest prime factor
Problem 3
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

http://projecteuler.net/problem=3

"""

from __future__ import division

import numpy as np

print "This solution is too slow for the input -- see the other one in here."

def is_prime(value):
    """ Checks if current value is prime. Returns True or False. """

    if value < 2: raise ValueError

    for i in range(2, value):
        if value % i == 0:
            return False

    return True

# Revise this - use a sieve!
def primes_up_to(value):
    """ 
    Generates a list of all primes less than or equal to `value`. 

    An implementation of the Sieve of Eratosthenes.
    
    """

    if value < 2: raise ValueError

    # Start with two and all the odd numbers.
    possible_primes = [2] + range(3, value+1, 2)
    primes = set(possible_primes)

    for i in possible_primes:

        if i in primes:

            # Remove all the MULTIPLES of i (but not i itself!)
            for j in range(2*i, value+1, i):
                primes.discard(j)

    return primes

def prime_factors_of(value):
    """ Returns all prime factors of `value`. """

    # Okay, so we need to "solve" two problems here:
    # is a given number a factor of `value`?
    #  and
    # is a given number PRIME?

    # I think the simplest non-stupid approach is to generate all 
    # FACTORS OF VALUE, and then check to see which are prime!
    # actually, a cute approach would be to start from the top down
    # and just return the first one. we'll see if i need that optimization.
    # (don't optimize prematurely!)

    # WELP. I tried to generate all primes up to value//2! what a mistake.
    # or was it? maybe it was just a bad implementation of prime-finding?

    factors = []

    for i in range(2, value//2):
        if value % i == 0:
            factors.append(i)

    prime_factors = []
    
    for i in factors:
        if is_prime(i):
            prime_factors.append(i)

    return prime_factors
    
assert set(prime_factors_of(13195)) == set([5, 7, 13, 29])
assert max(prime_factors_of(13195)) == 29

assert primes_up_to(2) == set([2])

#print max(prime_factors_of(600851475143))
