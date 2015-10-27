import random
# This is a Hackbright exercise. The docstring and doctests were provided 
# Hackbright. I coded the lucky_numbers function and added comments
# to the doc string describing the algorithm used

def lucky_numbers(n):
    """Return n unique random numbers from 1-10 (inclusive).

    Given the numbers 1-10, return `n` random numbers, making sure
    to never return the same number twice. You can trust that this
    function will never be called with n < 0 or n > 10.

    It's tricky to test random functions! However, we can make sure
    asking for zero numbers gives us an empty list:

        >>> lucky_numbers(0)
        []

    And if we ask for all numbers, we shouldn't get any repeats:

        >>> sorted(lucky_numbers(10))
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    Method: 
    Construct return list of integers in a loop until a 
    the return list contains n integers:
        1. Generate a random index 
        2. Use this index to pop an integer from the list of integers 1-10
        3. Add this integer to the return list of integers 
    """
    
    integer_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    return_list = []

    while n > 0:
        random_index = random.randint(0,n-1)
        new_int = integer_list.pop(random_index)
        return_list.append(new_int)
        n -= 1

    return return_list

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. GREAT!\n"
