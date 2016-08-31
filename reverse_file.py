def reverse_file(in_file, out_file):
	''' Read input file and write file with lines in reversed order
	    @param [String] in_file Path/name of input file
	    @param [String] out_file Path/name of output file 
	'''
	f = open(in_file)
	f_lines = f.readlines()
	reverse_file = open(out_file, "w")
	for i in range(len(f_lines) - 1, -1, -1):
		reverse_file.write(f_lines[i])
	f.close()

def print_file(file_name):
	''' Print a file
	    @param [String] file_name Path/name of text file to be printed 
	'''
	f = open(file_name)
	for line in f:
		print(line)
	f.close()

# Print input file, write reversed file, print reversed file
input_file = "test.txt"
output_file = "reverse_file.txt"

print("Original file: {}".format(input_file))
print_file(input_file)

reverse_file(input_file, output_file)
print("Reversed file: {}".format(output_file))
print_file(output_file)


