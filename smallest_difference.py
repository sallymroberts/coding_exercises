class SmallestDifference(object):
    def __init__(self, num_list, k):
        """ Accept: num_list = List of integers
                    k = Length of sequence: a subsetted list of num_list
            Calculate: answer = minimum possible value for max(sequence) - min(sequence)
        """
        # Sort the list and initialize smallest difference
        num_list_sorted = sorted(num_list)
        smallest_dif = num_list_sorted[-1] - num_list_sorted[0]
        
        # Find smallest difference among all possible consecutive sequences of length k for sorted list
        for i in range(len(num_list_sorted)-k+1):
          sequence = num_list_sorted[i:i+k]
          cur_dif = max(sequence) - min(sequence)
          if cur_dif < smallest_dif:
            smallest_dif = cur_dif
        
        # Set answer
        self.answer = smallest_dif

