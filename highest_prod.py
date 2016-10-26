def highest_product(list_of_ints):
	""" Get highest product using 3 integers in list of integers
		Arguments: list_of_ints [List] list of 3 or more integers

		Returns: [Integer] Highest product from 3 integers in list
	"""
	# Build lists of highest 3 positive integers,
	# 				highest 3 negative integers,
	#               lowest  3 negative integers
	#               Boolean for zero exists in list
	highest_pos = []
	highest_neg = []
	lowest_neg = []
	zero_int_exists = False

	for i in range(len(list_of_ints)):
		if list_of_ints[i] == 0:
			zero_int_exists = True

		elif list_of_ints[i] > 0:
			if len(highest_pos) < 3:
				highest_pos.append(list_of_ints[i])
			elif list_of_ints[i] > min(highest_pos):
				highest_pos.remove(min(highest_pos))
				highest_pos.append(list_of_ints[i])

		else:   # list_of_ints[i] < 0
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

	print("\n", list_of_ints, "\n", 
		zero_int_exists, highest_pos, lowest_neg, highest_neg)

	# Calculate possible positive products
	highest_pos.sort()
	lowest_neg.sort()
	highest_neg.sort()

	if len(highest_pos) >= 3:
		pos_prod_with_pos_only = highest_pos[-1] * highest_pos[-2] * highest_pos[-3]

	if len(lowest_neg) == 2 and len(highest_pos) >= 1:
		pos_prod_with_neg = lowest_neg[0] * lowest_neg[1] * highest_pos[-1]

	if len(highest_pos) >= 3:
		if len(lowest_neg) < 2:
			return pos_prod_with_pos_only
		elif len(lowest_neg) == 2:
			if pos_prod_with_neg > pos_prod_with_pos_only:
				return pos_prod_with_neg
			else:
				return pos_prod_with_pos_only

	elif len(highest_pos) >= 1 and len(lowest_neg) == 2:
		return pos_prod_with_neg

	elif zero_int_exists:
		return 0

	else:
		return "answer is negative"

# Tests
# Simple list of positive integers, includes zero, duplicate positive & negative integers
ints = [4, 7, 2, 8, -10, 8, 15, 0, -2, -10, -1, -3, -5] 
print(highest_product(ints))

ints = [-2, -5, 0, 4]
print(highest_product(ints))

ints = [-2, -5, 4, 3]
print(highest_product(ints))

ints = [-2, 0, 4, 3]
print(highest_product(ints))

ints = [-2, -5, -3, -6]
print(highest_product(ints))

ints = [-2, 1, 3]
print(highest_product(ints))



# # List of 3 integers
# ints = [4, 7, 2] 
# print("Expect 56: ", highest_product(ints))