def get_products_of_all_ints_except_at_index(ints):
	""" Get products of all integers in list, except integer at index

		For each index, find product of every integer except integer at that index.
		Example: Input is [1, 7, 3, 4], returns [84, 12, 28, 21]

		Argument: 
		integers [List] List of integers

		Returns: [List] List of products 
	"""
	# Construct list of products of integers before each element
	before_products = []
	for i in range(len(ints)):
		if i == 0:
			before_products.append(1)
		else:
			before_products.append(ints[i-1] * before_products[i-1])

	products = [None] * len(ints)
	
	product_after = 1

	# Loop through integers backwards, building list of products
	for i in range(len(ints) - 1, -1, -1):
		products[i] = before_products[i] * product_after
		product_after *= ints[i]

	return products

ints = [5, 7, 3, 4] # products = [84, 60, 140, 105]
prods = get_products_of_all_ints_except_at_index(ints)
print(prods)