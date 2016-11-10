def is_num_in_list(ints, num):
    """ Find num in sorted list of integers
        Arguments: 
        ints [List]    Sorted list of integers
        num  [Integer] Integer to check if in list
        
        Returns: [Boolean] True if integer is found in list
                           False if integer is not found in list
    """
    # Special cases
    # Empty list cannot contain number
    if len(ints) == 0:
        return False

    # Number not within upper/lower bounds of sorted integers
    if num < ints[0] or num > ints[-1]:
        return False

    # Initialize upper/lower/middle indices 
    upper_index = len(ints) - 1
    lower_index = 0
    middle_index = int(len(ints) / 2)

    # Check num above/below midpoint, 
    # Keep setting new midpoint
    while True:
        if num == ints[upper_index] or num == ints[lower_index]:
            return True
        elif num == ints[middle_index]:
            return True
        elif upper_index - lower_index <= 1:
            return False
        elif num > ints[middle_index]:
            lower_index = middle_index
        else:
            upper_index = middle_index

        middle_index = int((upper_index + lower_index) / 2)

# Tests
print("*" * 80)

ints = []
# Empty list
num = 5
print("Empty sorted integers list")
print("num:", num, "ints:", ints)
print(" Expect: False", 
    "\n", "Actual:", is_num_in_list(ints, num))
print()

# List with 1 element, num in list
ints = [2]
num = 2
print("List with 1 element, num in list")
print("num:", num, "ints:", ints)
print(" Expect: True", 
    "\n", "Actual:", is_num_in_list(ints, num))
print()

# List with 1 element, num not in list
num = 7
print("List with 1 element, num in list")
print("num:", num, "ints:", ints)
print(" Expect: False", 
    "\n", "Actual:", is_num_in_list(ints, num))
print()

ints = [-10, -4, 0, 5, 7, 100, 300, 503, 1000, 1002]

# num in bottom half
num = 5
print("num in bottom half of sorted integers list")
print("num:", num, "ints:", ints)
print(" Expect: True", 
    "\n", "Actual:", is_num_in_list(ints, num))
print()

# num in top half
print("num in top half of sorted integers list")
num = 503
print("num:", num, "ints:", ints)
print(" Expect: True", 
    "\n", "Actual:", is_num_in_list(ints, num))
print()

# first num in list
print("num is first integer in sorted integers list")
num = -10
print("num:", num, "ints:", ints)
print(" Expect: True", 
    "\n", "Actual:", is_num_in_list(ints, num))
print()

# last num in list
print("num is last integer in sorted integers list")
num = 1002
print("num:", num, "ints:", ints)
print(" Expect: True", 
    "\n", "Actual:", is_num_in_list(ints, num))
print()

# last num in list
print("num is higher than highest integer in integers list")
num = 11002
print("num:", num, "ints:", ints)
print(" Expect: False", 
    "\n", "Actual:", is_num_in_list(ints, num))
print()

# num less than minimum integer in list
print("num is less than lowest integer in integers list")
num = -215
print("num:", num, "ints:", ints)
print(" Expect: False", 
    "\n", "Actual:", is_num_in_list(ints, num))
print()

# num within list bounds, not in list
print("num within bounds of integers list, but not in list")
num = 505
print("num:", num, "ints:", ints)
print(" Expect: False", 
    "\n", "Actual:", is_num_in_list(ints, num))
print()

# num within list bounds, not in list
print("num within bounds of integers list, but not in list")
num = -1
print("num:", num, "ints:", ints)
print(" Expect: False", 
    "\n", "Actual:", is_num_in_list(ints, num))
print()

ints = [-10, -4, 0, 5, 7, 100, 300, 503, 1000]

# Integer list has odd number of elements, num not in list
num = 101
print("Integer list has odd number of elements, num not in list")
print("num:", num, "ints:", ints)
print(" Expect: False", 
    "\n", "Actual:", is_num_in_list(ints, num))
print()

# Integer list has odd number of elements, num is middle element
num = 7
print("Integer list has odd number of elements, num is middle element")
print("num:", num, "ints:", ints)
print(" Expect: True", 
    "\n", "Actual:", is_num_in_list(ints, num))
print()

# Integer list has odd number of elements, num is in upper half
num = 503
print("Integer list has odd number of elements, num in upper half")
print("num:", num, "ints:", ints)
print(" Expect: True", 
    "\n", "Actual:", is_num_in_list(ints, num))
print()

# Integer list has odd number of elements, num is in lower half
num = -4
print("Integer list has odd number of elements, num in lower half")
print("num:", num, "ints:", ints)
print(" Expect: True", 
    "\n", "Actual:", is_num_in_list(ints, num))
print()