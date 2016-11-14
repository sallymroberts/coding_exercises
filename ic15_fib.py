fibs = {0: 0, 1: 1}

def get_fib(n):
    """ Get nth fibonacci number
        Arguments: 
        n [Integer] index of fibonacci number 
        Returns: [Integer] nth number in fibonacci sequence
    """
    if n in fibs:
        return fibs[n]
    else:
        fibs[n] = get_fib(n-1) + get_fib(n-2)
        return fibs[n]

# Tests

print("n: 0", "\n", "Expect: 0", "\n", "Actual:", get_fib(0))
print()

print("n: 1", "\n", "Expect: 1", "\n", "Actual:", get_fib(1))
print()

print("n: 2", "\n", "Expect: 1", "\n", "Actual:", get_fib(2))
print()

print("n: 5", "\n", "Expect: 5", "\n", "Actual:", get_fib(5))
print()

print("n: 10", "\n", "Expect: 55", "\n", "Actual:", get_fib(10))
print()

print("n: 100", "\n", "Expect: 354224848179261915075", "\n", "Actual:", get_fib(100))
print()

# print compute(3), compute(3) == 2
# print compute(5), compute(5) == 5  
# print compute(10), compute(10) == 55   
# print compute(100), compute(100) == 354224848179261915075