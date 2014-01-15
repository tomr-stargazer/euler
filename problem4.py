"""
Largest palindrome product
Problem 4
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.

Find the largest palindrome made from the product of two 3-digit numbers.

http://projecteuler.net/problem=4

"""

def is_palindrome(number):
    """ Checks if a number is a palindrome. """
    
    if str(number) == str(number)[::-1]:
        return True
    else:
        return False

def find_all_palindrome_products_of_digits(digits):
    """
    Finds all palindrome products of two `digits`-long numbers.
    
    """

    palindromes = []

    for i in range(1,10**digits):

        n_1 = 10**digits - i

        for j in range(1,i+1):

            n_2 = 10**digits - j

            if is_palindrome(n_1*n_2):

                palindromes.append(n_1*n_2)

            if (n_1 < 10**(digits-1)) or (n_2 < 10**(digits-1)):
                break
        if (n_1 < 10**(digits-1)) or (n_2 < 10**(digits-1)):
            break

    return palindromes

assert max(find_all_palindrome_products_of_digits(2)) == 9009

print max(find_all_palindrome_products_of_digits(3))
