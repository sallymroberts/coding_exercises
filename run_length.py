def cvt_run_length(input_string):
    """ Convert a string into run length format:
        Input: a string
        Return: a string in run length format

        Run length format is a form of data compression in which runs of data
        (sequences in which the same data value occurs in consecutive data 
        elements) are stored as a single data value and count. 
        
    >>> cvt_run_length('ww    rrr')
    '2w4 3r'
    >>> cvt_run_length('')
    ''
    >>> cvt_run_length('aaabbbc')
    '3a3b1c'
           
    """
    
    if input_string == "": 
        return ""
    else:
        out_string = ""
        count = 0
        current_letter = input_string[0]
    
    for i in range(0, len(input_string)):
        if input_string[i] == current_letter:
            count += 1
        else:
            out_string = out_string + str(count) + current_letter
            current_letter = input_string[i]
            count = 1
    
    if count > 0:
        out_string = out_string + str(count) + current_letter
                
    return out_string    

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n All tests passed\n"