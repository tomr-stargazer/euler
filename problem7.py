"""
10001st prime
Problem 7
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?

http://projecteuler.net/problem=7

"""

from __future__ import division

import numpy as np
from scipy.optimize import minimize_scalar

def search_limit_for_k_primes(k):
    """ Gives the ceiling you'll need to search to in order to find k primes. """

    # The Prime Number Theorem shows us that the number of primes P 
    # lower than N is approximately 
    # P(n) \approx N / ln(N).    

    # This is the deviation from \pi(n) = n / ln(n) -- we want to make it zero.
    pi_deviation = lambda n: np.abs(k - n/np.log(n))

    limit = np.ceil(np.sqrt(2) * minimize_scalar(pi_deviation, method='bounded', 
                                                 bounds=[k, k**2]).x)

    return int(limit)+5

def kth_prime(k):
    """ Finds the kth prime number. """

    search_limit = search_limit_for_k_primes(k)

    possible_primes = [2] + range(3, search_limit, 2)
    primes = set(possible_primes)

    list_of_primes = [2]

    for n in possible_primes:

        if n in primes:

            for kn in range(2*n, search_limit, n):
                primes.discard(kn)

    assert len(primes) >= k

    return sorted(list(primes))[k-1]
    
assert kth_prime(6) == 13

print kth_prime(10001)
