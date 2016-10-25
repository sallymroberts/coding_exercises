def spiral_print(matrix):
    """ Print a 2-dimensional matrix in a spiral.
        Start with top row, moving to the right.

        Input: matrix [List] 2-dimensional matrix of positive integers
        Return: Returns None

        TEST CASES
        
        Square matrix (3 x 3), odd number of rows & columns
        >>> matrix = [[1, 2, 3],
        ...           [4, 5, 6],
        ...           [7, 8, 9],
        ...           [10,11, 12]]
        >>> spiral_print(matrix)
        1 2 3 6 9 12 11 10 7 4 5 8 

        Square matrix (4 x 4), even number of rows & columns
        >>> matrix = [[1, 2, 3, 4],
        ...           [5, 6, 7, 8],
        ...           [9, 10, 11, 12],
        ...           [13, 14, 15, 16]]
        >>> spiral_print(matrix)
        1 2 3 4 8 12 16 15 14 13 9 5 6 7 11 10 


        Not square matrix (5 x 3), odd number of rows & columns
        >>> matrix = [[1, 2, 3, 4, 5],
        ...           [6, 7, 8, 9, 10],
        ...           [11, 12, 13, 14, 15]]
        >>> spiral_print(matrix)
        1 2 3 4 5 10 15 14 13 12 11 6 7 8 9 

        Not square matrix (3 x 4), even number of rows, odd number of columns
        >>> matrix = [[1, 2, 3],
        ...           [4, 5, 6],
        ...           [7, 8, 9],
        ...           [10,11, 12]]
        >>> spiral_print(matrix)
        1 2 3 6 9 12 11 10 7 4 5 8 

        Matrix has only 2 rows (2 x 4)
        >>> matrix = [[1, 2, 3, 4],
        ...           [5, 6, 7, 8]]
        >>> spiral_print(matrix)
        1 2 3 4 8 7 6 5 

        Matrix has only 1 row (1 x 4)
        >>> matrix = [[1, 2, 3, 4]]
        >>> spiral_print(matrix)
        1 2 3 4 

        Matrix has only 1 column (4 x 1)
        >>> matrix = [[1],
        ...           [2],
        ...           [3],
        ...           [4]]
        >>> spiral_print(matrix)
        1 2 3 4 

        Matrix has 1 row and 1 column (1 x 1)
        >>> matrix = [[1]]
        >>> spiral_print(matrix)
        1 

        Matrix paramater is invalid: Empty list
        >>> matrix = []
        >>> spiral_print(matrix)
        Matrix must have at least 1 row and 1 column

        Matrix parameter is invalid: List containing an empty list
        >>> matrix = [[]]
        >>> spiral_print(matrix)
        Matrix must have at least 1 row and 1 column
    """
    if len(matrix) < 1:
        print("Matrix must have at least 1 row and 1 column")
        return
    elif len(matrix[0]) < 1:
        print ("Matrix must have at least 1 row and 1 column")
        return

    col_max_ind = len(matrix[0]) - 1
    row_max_ind = len(matrix) - 1
    row_min_ind = 0
    col_min_ind = 0
    num_elem = len(matrix[0]) * len(matrix)

    i = 0 # row index
    j = 0 # col index
    direction = "right"
    count = 0

    while count < num_elem:

        print(matrix[i][j], end=" ")
        count += 1

        if direction == "right":
            if j < col_max_ind:
                j += 1
            else:
                row_min_ind += 1
                direction = "down"
                i += 1
        elif direction == "down":
            if i < row_max_ind:
                i += 1
            else:
                col_max_ind -= 1
                direction = "left"
                j -= 1
        elif direction  == "left":
            if j > col_min_ind:
                j -= 1
            else:
                row_max_ind -= 1
                direction = "up"
                i -= 1
        elif direction == "up":
            if i > row_min_ind:
                i -= 1
            else:
                row_min_ind += 1
                direction = "right"
                j += 1

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. GREAT!\n")