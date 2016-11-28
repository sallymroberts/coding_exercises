def reverse_words(chars):
    """ Reverse words 'in place', using character list
        Arguments:
        phrase [String]

        Instructions include: 
              * Assume no punctuation, only words and spaces
              * Practice reversing "in place" 
              * Because Python strings are immutable:
                  Convert to list of characters
                  Reverse words in that list
                  Join reversed word list into string

        Returns:
        reversed_phrase [String] input string with words in reversed order
    """
    if chars == "":
        return ""
    rev_chars_list = list(reverse_string(chars))

    cur_word_start_index = 0

    for i in range(len(rev_chars_list)):
        if rev_chars_list[i] == " " or i == (len(rev_chars_list)):
            rev_word_chars = reverse_string(rev_chars_list[cur_word_start_index:i])
            rev_chars_list[cur_word_start_index:i] = rev_word_chars
            cur_word_start_index = i + 1

    # process last word
    rev_word_chars = reverse_string(rev_chars_list[cur_word_start_index:i+1])
    rev_chars_list[cur_word_start_index:i+1] = rev_word_chars

    return "".join(rev_chars_list)

def reverse_string(characters):
    """ Reverse string 'in place', using character list
        Arguments:
        characters [String]

        Returns:
        reversed_chars [String] input string in reversed order

    """
    phrase_chars = list(characters)
    phrase_half_len = int(len(phrase_chars)/2)
    
    for i in range(phrase_half_len):
        save_char = phrase_chars[i]
        phrase_chars[i] = phrase_chars[-(i+1)]
        phrase_chars[-(i+1)] = save_char

    reversed_chars = "".join(phrase_chars)
    return reversed_chars  
# Tests
# String with odd length
print("Phrase with odd length: 'words few a is This'")
chars = "words few a is This"
print("Expect: This is a few words")
print("Actual:", reverse_words(chars))

# String with even length
print()
print("Phrase with even length: 'find you will pain only go you recordings security the into If'")
chars = 'find you will pain only go you recordings security the into if'
print("Expect: If into the security recordings you go only pain will you find")
print("Actual:", reverse_words(chars))

# Empty string
print()
chars = ""
print("Empty string")
print("Expect: ")
print("Actual:", reverse_words(chars))

# String with 1 character
print()
chars = "A"
print("String with 1 character")
print("Expect: A")
print("Actual:", reverse_words(chars))