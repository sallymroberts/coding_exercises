def reverse_string(input_string):
	""" Create a function to reverse a string using a stack
		Note: I reused doctests I wrote in reverse_string.py, 
	    	  an exercise to reverse a string using recursion

	Test string with a length that is an even number:
	>>> reverse_string("123456")
	'654321'

	Test string with a length that is an odd number:
	>>> reverse_string("1234567")
	'7654321'

	Test a string that includes spaces:
	>>> reverse_string("This is a test of reversal")
	'lasrever fo tset a si sihT'

	Test an empty string:
	>>> reverse_string("")
	''

	Test a string of length 1:
	>>> reverse_string("2")
	'2'
	"""

# Handle empty string or string of length 1 by returning the input string
# Otherwise:
#   1. Convert input string to list of characters
# 	2. Push the character list onto a character stack
#   3. Reverse the characters by popping the characters from the stack 
#      onto a reverse character list
#   4. Join the reverse character list into a string and return that string
#   
# For the input string "ABCD", these steps produce the following output:
#	1. character list:  ["A", "B", "C", "D"]
#   2. character stack: ["A", "B", "C", "D"]
#   3. reverse character list: ["D", "C", "B", "A"]
#   4. reverse string: "DCBA"

	if len(input_string) <= 1:
		return input_string
	
	else: 
		char_list = list(input_string)
		char_stack = Stack()

		for char in char_list:
			char_stack.push(char)

		reverse_char_list = []

		while char_stack.isEmpty() is False:
			reverse_char_list.append(char_stack.pop())

		join_str = ""
		reverse_str = join_str.join(reverse_char_list)
		return reverse_str

class Stack(object):
	"""Use Stack class definition from Problem Solving and Algorithms"""
	
	def __init__(self):
		self.items = []

	def isEmpty(self):
		return self.items == []

	def push(self, item):
		self.items.append(item)

	def pop(self):
		return self.items.pop()

	def peek(self):
		return self.items[len(self.items)-1]

	def size(self):
		return len(self.items)

if __name__ == "__main__":
	import doctest
	if doctest.testmod().failed == 0:
		print "\n All tests passed\n"
