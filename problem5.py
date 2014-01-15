"""
Smallest multiple
Problem 5
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

http://projecteuler.net/problem=5

"""

from problem3 import find_largest_prime_factor

def find_smallest_evenly_divided_number_for(value):

    running_product = 1

    for i in range(1,value+1):

        if running_product % i != 0:
            running_product *= find_largest_prime_factor(i)

            assert running_product % i == 0

    return running_product

assert find_smallest_evenly_divided_number_for(10) == 2520

print find_smallest_evenly_divided_number_for(20)
