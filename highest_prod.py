def highest_product(list_of_ints):
	""" Get highest product using 3 integers in list of integers
		Arguments: list_of_ints [List] list of 3 or more integers,
				       can include zero, negative & positive integers

		Returns: [Integer] Highest product from 3 integers in list
		                   Product can be zero, positive or negative
	"""
	# Initialize lists of highest positive integers, # max len 3
	#				      lowest  positive integers  # max len 2
	# 				      highest negative integers, # max len 2
	#                     lowest  negative integers  # max len 3
	#                	  Boolean for zero exists in list
	highest_pos = []
	highest_neg = []
	lowest_neg = []
	lowest_pos = []
	zero_int_exists = False

	# Loop thru input list of integers:
	# 	Build lists initialized above, and set zero_int_exists

	for i in range(len(list_of_ints)):
		# Process zero
		if list_of_ints[i] == 0:               
			zero_int_exists = True

		# Process positive integer
		elif list_of_ints[i] > 0:
			if len(highest_pos) < 3:
				highest_pos.append(list_of_ints[i])
			elif list_of_ints[i] > min(highest_pos):
				highest_pos.remove(min(highest_pos))
				highest_pos.append(list_of_ints[i])

			if len(lowest_pos) < 2:
				lowest_pos.append(list_of_ints[i])
			elif list_of_ints[i] < max(lowest_pos):
				lowest_pos.remove(max(lowest_pos))
				lowest_pos.append(list_of_ints[i])
		# Process negative integer
		else:
			if len(lowest_neg) < 2:
				lowest_neg.append(list_of_ints[i])
			else:
				if list_of_ints[i] < max(lowest_neg):
					lowest_neg.remove(max(lowest_neg))
					lowest_neg.append(list_of_ints[i])

			if len(highest_neg) < 3:
				highest_neg.append(list_of_ints[i])
			else:
				if list_of_ints[i] > min(highest_neg):
					highest_neg.remove(min(highest_neg))
					highest_neg.append(list_of_ints[i]) 

	# Sort lists
	highest_pos.sort()
	lowest_pos.sort()
	lowest_neg.sort()
	highest_neg.sort()

	# Print input list, sub-lists
	print("\n", list_of_ints)
	print("zero_int_exists, highest/lowest pos, highest/lowest neg: ", 
		"\n", zero_int_exists, highest_pos, lowest_pos, highest_neg, lowest_neg)

	# Build high product candidates list
	possible_high_prods = []

	# Add positive products to high product candidates list
	if len(highest_pos) == 3:
		possible_high_prods.append(highest_pos[0] * highest_pos[1] * highest_pos[2])

	if len(lowest_neg) == 2 and len(highest_pos) >= 1:
		possible_high_prods.append(lowest_neg[0] * lowest_neg[1] * highest_pos[-1])

	# If no high product candidates, append zero and negative products to high product candidates
	if len(possible_high_prods) == 0:
		if zero_int_exists:
			possible_high_prods.append(0)
		else:
			if len(lowest_pos) == 0:
				possible_high_prods.append(highest_neg[0] * highest_neg[1] * highest_neg[2])
			else:
				possible_high_prods.append(lowest_pos[0] * lowest_pos[1] * lowest_neg[-1])
	
	return max(possible_high_prods)

# Tests
# Simple list of positive integers, includes zero, duplicate positive & negative integers
# 2 possible positive candidates (-10 * -10 * 15 = 1500), (7 * 8 * 15 = 840)
ints = [4, 7, 2, 8, -10, 8, 15, 0, -2, -10, -1, -3, -5] 
print("Expect 1500: Got", highest_product(ints))

# Positive product from 2 negative integers, 1 positive integer
# Only 1 possible positive candidate 
ints = [-2, -5, 0, 4]
print("Expect 40: Got", highest_product(ints))

ints = [-2, -5, 4, 3]
print("Expect 40: Got", highest_product(ints))

ints = [-2, 0, 4, 3]
print("Expect zero: Got", highest_product(ints))

ints = [-2, -5, -3, -6]
print("Expect -30: Got", highest_product(ints))

ints = [-2, 1, 3]
print("Expect -6: Got", highest_product(ints))