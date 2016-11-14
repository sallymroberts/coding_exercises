def two_movies_for_flight_exist(flight_length, movie_lengths):
    """ Check if two movies match flight length
        Arguments: 
        flight_length [Integer] Length of flight in minutes
        movie_lengths [List] Integers representing movie lengths in minutes
        Returns: [Boolean] True: There are 2 different movies whose combined 
                                 lengths equals flight length
                           False: There are not 2 movies meeting condition
    """
    mov_lens = set()

    for mov_len in movie_lengths:
        other_movie = flight_length - mov_len
        if other_movie in mov_lens:
            return True
        else:
            mov_lens.add(mov_len)

    return False

# Tests

# Two movies with different lengths equal flight length
flight_length = 230
movie_lengths = [95, 80, 75, 60, 120, 85, 110]
print("Two movies with different lengths equal flight length")
print("flight length, movie lengths:", flight_length, movie_lengths)
print(" Expect: True", "\n", "Actual:", two_movies_for_flight_exist(flight_length, movie_lengths))
print()

# Two movies with same length equal flight length
flight_length = 150
movie_lengths = [95, 80, 75, 60, 75, 85, 110]
print("Two movies with same length equal flight length")
print("flight length, movie lengths:", flight_length, movie_lengths)
print(" Expect: True", "\n", "Actual:", two_movies_for_flight_exist(flight_length, movie_lengths))
print()

# No two combined movie lengths equal flight length
flight_length = 210
movie_lengths = [95, 80, 75, 60, 75, 85, 110]
print("No two combined movie lengths equal flight length")
print("flight length, movie lengths:", flight_length, movie_lengths)
print(" Expect: False", "\n", "Actual:", two_movies_for_flight_exist(flight_length, movie_lengths))
print()

# No two combined movie lengths equal flight length
# One movie equals half flight length
flight_length = 120
movie_lengths = [95, 80, 75, 60, 75, 85, 110]
print("No two combined movie lengths equal flight length")
print("One movie equals half flight length")
print("flight length, movie lengths:", flight_length, movie_lengths)
print(" Expect: False", "\n", "Actual:", two_movies_for_flight_exist(flight_length, movie_lengths))
print()