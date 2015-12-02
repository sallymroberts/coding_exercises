def cvt_int_to_str(inp_integer):
	''' Convert integer to formatted string
		input integer, output string formatted as number

	>>> print "123 converts to: ", cvt_int_to_str(123)
	123 converts to:  123

	>>> print "1234 converts to: ", cvt_int_to_str(1234)
	1234 converts to:  1,234

	>>> print "123456 converts to: ", cvt_int_to_str(123456)
	123456 converts to:  123,456

	>>> print "1234567890 converts to: ", cvt_int_to_str(1234567890)
	1234567890 converts to:  1,234,567,890
	
	>>> print "1 converts to: ", cvt_int_to_str(1)
	1 converts to:  1

	'''
	init_string = str(inp_integer)
	modulus = len(init_string) % 3

	if modulus == 0:
		out_string = ""
	else:
		out_string = init_string[0:modulus] + ","
		
	start = modulus
	stop = modulus + 3
	
	while stop <= len(init_string):
		out_string = out_string + init_string[start:stop] + ","
		start += 3
		stop += 3
	
	out_string = out_string.rstrip(",")    
	return out_string

if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print "\n All tests passed\n"
