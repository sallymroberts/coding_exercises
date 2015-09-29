def reverse_string(input_string):
	""" Create a recursive function to reverse a string
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
	
	if len(input_string) <= 1:
		return input_string
	else:
		return input_string[-1] + reverse_string(input_string[0:-1])

if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print "\n All tests passed\n"
