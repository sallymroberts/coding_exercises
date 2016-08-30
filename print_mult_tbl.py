def print_mult():
    ''' Print multiplication tables
    '''

    # Formatted string with layout for each row
    layout = "{:>4}{:>6}{:>4}{:>4}{:>4}{:>4}{:>4}{:>4}{:>4}{:>4}{:>4}{:>4}{:>4}"
    # Print column heading rows
    print(layout.format("",1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))
    under = "   :" + 50 * "-"
    print(under)
    
    # Print multiplication tables detail
    for i in range(1,13):
        print(layout.format(str(i) + ":", i, i*2, i*3, i*4, i*5, i*6, i*7, i*8, i*9, i*10, i*11, i*12))


print_mult()