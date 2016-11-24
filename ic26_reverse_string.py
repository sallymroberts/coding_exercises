def reverse_string(phrase):
    """ Reverse string 'in place', using character list
        Arguments:
        phrase [String]

        Note: Practice reversing "in place"
              Because Python strings are immutable:
              Convert to list of characters
              Reverse in place
              Join characters into reversed string

        Returns:
        reversed_phrase [String] input string in reversed order

    """
    phrase_chars = list(phrase)
    phrase_half_len = int(len(phrase_chars)/2)
    
    for i in range(phrase_half_len):
        save_char = phrase_chars[i]
        phrase_chars[i] = phrase_chars[-(i+1)]
        phrase_chars[-(i+1)] = save_char

    reversed_phrase = "".join(phrase_chars)
    return reversed_phrase

# String with odd length
phrase = "This is a few words"
print("Phrase with odd length: 'This is a few words'")
string_reversed = reverse_string(phrase)
print("Expect: sdrow wef a si sihT")
print("Actual:", string_reversed)

# String with even length
print()
phrase = "This is four words"
print("Phrase with even length: 'This is four words'")
string_reversed = reverse_string(phrase)
print("Expect: sdrow ruof si sihT")
print("Actual:", string_reversed)

# Empty string
print()
phrase = ""
print("Empty string")
string_reversed = reverse_string(phrase)
print("Expect: ")
print("Actual:", string_reversed)

# String with 1 character
print()
phrase = "A"
print("String with 1 character")
string_reversed = reverse_string(phrase)
print("Expect: A")
print("Actual:", string_reversed)