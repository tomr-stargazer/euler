"""

Something about palindromes. 

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
        
def find_largest_palindrome_product_of_digits(digits):
    """ 
    Finds the largest palindrome product of two `digits`-long numbers. 

    """

    return max(find_all_palindrome_products_of_digits(digits))

assert find_largest_palindrome_product_of_digits(2) == 9009

print find_largest_palindrome_product_of_digits(3)
