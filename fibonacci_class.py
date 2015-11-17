# Create a class method to calculate the Fibonacci number.
#
# The Fibonacci sequence is a set of numbers that starts with a one or a zero,
# followed by a one, and proceeds based on the rule that each number 
# (called a Fibonacci number) is equal to the sum of the preceding two numbers.
#
# For example, the Fibonacci sequence, beginning with 0 as the index is:
#            Index: 0 1 2 3 4 5 6 7  8  9  10
# Fibonacci number: 0 1 1 2 3 5 8 13 21 34 55    

class Fib(object):
    
    def compute(self, result_index):
        ''' Calculate Fibonacci number
            Accept index, return Fibonacci number
        '''
        if result_index == 0:
            return 0
        elif result_index == 1:
            return 1
        else:
            
            next_to_last = 0
            last = 1
            result = 1
            
            for i in range(2, result_index):
                next_number = next_to_last + last
                next_to_last = last
                last = next_number
                
            next_number = next_to_last + last
            return next_number
        
fib_inst = Fib() 

# Print fibonacci numbers, testing that results are valid 

print [fib_inst.compute(0), fib_inst.compute(0) == 0]
print [fib_inst.compute(1), fib_inst.compute(1) == 1]
print [fib_inst.compute(3), fib_inst.compute(3) == 2]
print [fib_inst.compute(5), fib_inst.compute(5) == 5]
print [fib_inst.compute(10), fib_inst.compute(10) == 55]
