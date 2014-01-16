"""
Summation of primes
Problem 10
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

http://projecteuler.net/problem=10
"""

import numpy as np

def sum_primes_below(value):
    """ Sums all primes below an input value. """

    # let's try a sieve of Eratosthenes.
    
    possible_primes = [2] + range(3, value, 2)
    primes = set(possible_primes)

    for n in possible_primes:

        if n in primes:

            for kn in range(2*n, value, n):
                primes.discard(kn)

    print "There are %d primes below %d" % (len(primes), value)

    return np.sum(list(primes))

assert sum_primes_below(10) == 17

print sum_primes_below(int(2e6))
