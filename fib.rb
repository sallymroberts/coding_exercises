# Write a function fib() that takes an integer n
# and returns the nth fibonacci number

# The Fibonacci sequence is a set of numbers that starts with a one or a zero,
# followed by a one, and proceeds based on the rule that each number
# (called a Fibonacci number) is equal to the sum of the preceding two numbers.
#
# For example, the Fibonacci sequence, beginning with 0 as the index is:
#            Index: 0 1 2 3 4 5 6 7  8  9  10
# Fibonacci number: 0 1 1 2 3 5 8 13 21 34 55

# Write a function fib() that takes an integer n
# and returns the nth fibonacci number

def fib(n)
  if n == 0
    return 0
  elsif n == 1
    return 1
  end

  last = 1
  next_to_last = 0
  i = 2

  while i <=n
    cur_fib = last + next_to_last
    next_to_last = last
    last = cur_fib
    i +=1
  end
  return cur_fib
end

puts "fib(0) is #{fib(0)}"
puts "fib(1) is #{fib(1)}"
puts "fib(2) is #{fib(2)}"
puts "fib(3) is #{fib(3)}"
puts "fib(4) is #{fib(4)}"
puts "fib(5) is #{fib(5)}"
puts "fib(8) is #{fib(8)}"
puts "fib(10) is #{fib(10)}"