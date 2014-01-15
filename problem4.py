"""

Something about palindromes. 

"""

def is_palindrome(number):
    """ Checks if a number is a palindrome. """
    
    if str(number) == str(number)[::-1]:
        return True
    else:
        return False

def find_largest_palindrome_product_of_digits(digits):
    """ 
    Finds the largest palindrome product of two `digits`-long numbers. 

    """

    pass

assert find_largest_palindrome_product_of_digits(2) == 9009

print find_largest_palindrome_product_of_digits(3)
