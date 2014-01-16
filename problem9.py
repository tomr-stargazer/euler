"""
Special Pythagorean triplet
Problem 9
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a**2 + b**2 = c**2
For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

http://projecteuler.net/problem=9

"""

def find_pythagorean_triple(abc_sum):
    """ Finds the pythagorean triple where a+b+c = abc_sum. """

    # so, the largest value of 'a' can be is 332.
    for a in range(abc_sum//3):
        
        # smallest possible value of 'b' is a+1,
        # and the largest value of 'b' is 500 - a/2.
        for b in range(a + 1, abc_sum//2 - a//2):

            c = abc_sum - a - b

            if c**2 == a**2 + b**2:
                print "a: %d, b: %d, c: %d. Product: %d" % (a, b, c, a*b*c)
                return a*b*c


print find_pythagorean_triple(1000)


        
