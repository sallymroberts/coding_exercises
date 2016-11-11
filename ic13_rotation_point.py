def get_word_list_rotation_point(words):
    """ Get 'rotation point' in 'rotated' sorted word list
        Arguments: 
        words [List] Words sorted in alphabetical order, except 'rotated'
                     so that word closest to beginning of the alphabetic
                     can be in the middle
                     Example:
                     ['jungle', 'llama', 'peanut', 'zebra', 'ant', 'dog']
        Returns: [Integer] Index of word at alphabetical beginning
                     If word list is empty, returns None
                     From example above, return 4, index for 'ant'
    """
    # Handle special case of empty list
    if len(words) == 0:
        return None

    # Set bounds for indices to check
    high_index = len(words) - 1
    low_index = 0
  
    # Check middle word against words at upper/lower bounds
    # Use results to re-set upper or lower bound, to split
    # remaining elements to check in half
    while high_index - low_index > 1:
        mid_index = int((high_index + low_index) / 2)
        if words[mid_index] > words[high_index]:
            low_index = mid_index
        else:
            high_index = mid_index

    if high_index - low_index == 0:
            return high_index
    else:
        if words[low_index] < words[high_index]:
            return low_index
        else:
            return high_index

# Tests
print("*" * 80)

# Word list is empty
words = []
print("Word list is empty")
print("words:", words)
print(" Expect: None", "\n", "Actual:", get_word_list_rotation_point(words))
print()

# Word list has 1 element
words = ['fox']
print("Word list has 1 element")
print("words:", words)
print(" Expect: 0", "\n", "Actual:", get_word_list_rotation_point(words))
print()

# Word list has odd number of elements, rotation point is in upper half
words = ['jungle', 'llama', 'peanut', 'zebra', 'ant', 'dog', 'elephant']
print("Word list has odd number of elements, rotation point in upper half")
print("words:", words)
print(" Expect: 4", "\n", "Actual:", get_word_list_rotation_point(words))
print()

# Word list has even number of elements, rotation point is in upper half
words = ['fox', 'jungle', 'llama', 'peanut', 'zebra', 'ant', 'dog', 'elephant']
print("Word list has even number of elements, rotation point in upper half")
print("words:", words)
print(" Expect: 5", "\n", "Actual:", get_word_list_rotation_point(words))
print()

# Word list has odd number of elements, rotation point is in lower half
words = ['zebra', 'ant', 'dog', 'elephant', 'jungle', 'llama', 'peanut']
print("Word list has odd number of elements, rotation point in lower half")
print("words:", words)
print(" Expect: 1", "\n", "Actual:", get_word_list_rotation_point(words))
print()

# Word list has even number of elements, rotation point is in lower half
words = ['peanut', 'zebra', 'ant', 'dog', 'elephant', 'fox', 'jungle', 'llama']
print("Word list has even number of elements, rotation point in lower half")
print("words:", words)
print(" Expect: 2", "\n", "Actual:", get_word_list_rotation_point(words))
print()

# Rotation point is first element
words = ['ant', 'dog', 'elephant', 'fox', 'jungle', 'llama', 'peanut', 'zebra']
print("Rotation point is first element")
print("words:", words)
print(" Expect: 0", "\n", "Actual:", get_word_list_rotation_point(words))
print()

# Rotation point is last element
words = ['dog', 'elephant', 'fox', 'jungle', 'llama', 'peanut', 'rhino', 'zebra', 'ant']
print("Rotation point is last element")
print("words:", words)
print(" Expect: 8", "\n", "Actual:", get_word_list_rotation_point(words))
print()