# Print a 2-dimensional matrix in a spiral, beginning
# with the top row moving to the right
# TODO Work in progress, not working correctly

def spiral_print(matrix):
	row_max_ind = len(matrix[0]) - 1
	col_max_ind = len(matrix) - 1
	row_min_ind = 0
	col_min_ind = 0
	num_elem = len(matrix[0]) * len(matrix)

	i = 0 # row index
	j = 0 # col index
	direction = "right"
	count = 0

	while count <= num_elem:
		print(matrix[i][j], end = " ")
		count += 1

		if direction == "right":
			if j < col_max_ind:
				j += 1
			else:
				row_max_ind -= 1
				direction = "down"
				i += 1
		elif direction == "down":
			if i <= row_max_ind:
				i += 1
			else:
				col_max_ind -= 1
				direction = "left"
				j -= 1
		elif direction	== "left":
			if j > col_min_ind:
				j -= 1
			else:
				col_min_ind += 1
				direction = "up"
				i -= 1
		elif direction == "up":
			if i > row_min_ind:
				i -= 1
			else:
				row_max_ind -= 1
				direction = "right"
				j += 1

matrix = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12],
          [13, 14, 15, 16]]
spiral_print(matrix)  # should print 1 2 3 4 8 12 16 15 14 13 9 5 6 7 11 10












