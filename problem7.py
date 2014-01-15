"""
10001st prime
Problem 7
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?

http://projecteuler.net/problem=7

"""

def nth_prime(n):

    # How about something recursive:
    # find the first prime, make a list of all known primes.
    # then iterate upwards diffing everybody against the known list of primes.
    # when you hit the next one... append it to the list.
    # might be super slow. we'll see. But given that I don't know beforehand 
    # what ballpark the 10001st prime might be in, I don't know how I'd use
    # the sieve from earlier. 
    # except maybe with a while loop:  while
    # the list of primes is less than the desired length, do a thing
    # where you square the the highest prime and sieve through all those values
    # looking for nonprimes.

    pass

assert nth_prime(6) == 13

print nth_prime(10001)
