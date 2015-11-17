# Create a recursive function to calculate the Fibonacci number.
#
# The Fibonacci sequence is a set of numbers that starts with a one or a zero,
# followed by a one, and proceeds based on the rule that each number 
# (called a Fibonacci number) is equal to the sum of the preceding two numbers.
#
# For example, the Fibonacci sequence, beginning with 0 as the index is:
#            Index: 0 1 2 3 4 5 6 7  8  9  10
# Fibonacci number: 0 1 1 2 3 5 8 13 21 34 55    


# Create a dictionary to hold index as key and Fibonacci number as value,
# loading with the first two indices as special cases

fib_dict = {0:0, 
            1:1}

def compute(n):
    ''' Calculate Fibonacci number recursively
        Accept index, return Fibonacci number
        Store index, Fibonacci number in a dictionary.
        Retrieve Fibonacci numbers from dictionary to avoid 
        recalculating Fibonacci numbers from index 0.
    '''
    if n in fib_dict:
        return fib_dict[n]
    
    else:
        fib_dict[n] = compute(n-1) + compute(n-2)
        return fib_dict[n]

# Print fibonacci numbers, testing that results are valid

print compute(0), compute(0) == 0    
print compute(1), compute(1) == 1  
print compute(3), compute(3) == 2
print compute(5), compute(5) == 5  
print compute(10), compute(10) == 55   
print compute(100), compute(100) == 354224848179261915075