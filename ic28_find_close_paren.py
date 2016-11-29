def find_close_paren(phrase, open_paren_index):
    """ Find the corresponding close parentheses for an open parentheses
        Arguments:
        phrase            [String]  Containing open & close parentheses
        open_paren_index  [Integer] Index of an open parentheses in phrase

        Returns:
        close_paren_index [Integer] Index of corresponding close parentheses in phrase
    """
    open_parens_count = 0
    close_parens_count = 0

    # Handle errors:
    if phrase == "":
        return None

    if open_paren_index > len(phrase) - 1:
        return None

    if phrase[open_paren_index] != "(":
        return None

    # Loop thru phrase from open paren forward until finding matching close paren
    for i in range(open_paren_index, len(phrase)):
        if phrase[i] == "(":
            open_parens_count += 1
        elif phrase[i] == ")":
            close_parens_count += 1

        if open_parens_count == close_parens_count:
            return i

    # No matching parentheses found
    return None

# Tests
print("*" * 80)
# Phrase with multiple parentheses, match first open parentheses
print("Phrase with multiple parentheses, match first open parentheses")
phrase = "Sometimes (when I nest them (my parentheticals) too much (like this (and this))) they get confusing."
print("Expect: 79")
print("Actual:", find_close_paren(phrase, 10))

# Phrase with multiple parentheses, match second open parentheses
print()
print("Phrase with multiple parentheses, match second open parentheses")
phrase = "Sometimes (when I nest them (my parentheticals) too much (like this (and this))) they get confusing."
print("Expect: 46")
print("Actual:", find_close_paren(phrase, 28))

# Phrase with multiple parentheses, match last open parentheses
print()
print("Phrase with multiple parentheses, match last open parentheses")
#         0123456789 123456789 123456789 123456789 123456789 123456789 123456789 123456789
phrase = "Sometimes (when I nest them (my parentheticals) too much (like this (and this))) they get confusing."
print("Expect: 77")
print("Actual:", find_close_paren(phrase, 68))

# Phrase with one parentheses, close parentheses at end of phrase
print()
print("Phrase with one parentheses, close parentheses at end of phrase")
phrase = "Much to buy (shoes, socks, ribbons)"
print("Expect: 34")
print("Actual:", find_close_paren(phrase, 12))

# Phrase with one parentheses, close parentheses at end of phrase
print()
print("Phrase with one parentheses, close parentheses in middle of phrase")
phrase = "Much to buy (shoes, socks, ribbons) and more to sell"
print("Expect: 34")
print("Actual:", find_close_paren(phrase, 12))

# ERROR CONDITIONS, return None
# Empty string
print()
print("Phrase is empty string")
phrase = ""
print("Expect: None")
print("Actual:", find_close_paren(phrase, 0))

# Character at open paren index is not open parentheses
print()
print("Character at open paren index is not open parentheses")
phrase = "Much to buy (shoes, socks, ribbons) and more to sell"
print("Expect: None")
print("Actual:", find_close_paren(phrase, 33))

# Open paren index out of bounds
print()
print("Open paren index out of bounds")
phrase = "Much to buy (shoes, socks, ribbons) and more to sell"
print("Expect: None")
print("Actual:", find_close_paren(phrase, 85))

# Open parentheses has no close parentheses
print()
print("Open parentheses has no close parentheses")
phrase = "Much to buy (shoes, socks, ribbons and more to sell"
print("Expect: None")
print("Actual:", find_close_paren(phrase, 12))