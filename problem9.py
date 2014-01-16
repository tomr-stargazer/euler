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

# so, the largest value of 'a' can be 332.
# if we just do a double forloop of all the possible sums of three such digits to 

def is_pythagorean_triple(a, b, c):
    """ Tests whether a given triple is Pythagorean, i.e. obeys a**2+b**2=c**2."""

    return c**2 == a**2 + b**2

for a in range(333):

    for b in range(a+1, 500-a/2):

        c = 1000 - a - b

        assert c > b
        assert b > a

        if is_pythagorean_triple(a,b,c):
            print "a: %d, b: %d, c: %d. Product: %d" % (a, b, c, a*b*c)
            print "ANSWER ^ "

            print a*b*c



        
