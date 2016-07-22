# Create recursive function is_palindrome? to test if phrase is palindrome

# Check if phrase is palindrome
#   First, format string to remove punctuation and whitespace
# @param  [String] phrase may include whitespace and punctuation
# @return [Boolean] true = is palindrome, false = not palindrome
def is_pal?(phrase:)
  phrase = strip_string(phrase: phrase)
  return true if phrase.length <= 1
  return false unless phrase[0] == phrase[-1]
  is_pal?(phrase: phrase[1..-2])
end

# Strip string of punctuation and whitespace
# @param  [String] unformatted
# @return [String] formatted: no punctuation or whitespace, downcase
def strip_string(phrase:)
  unless phrase == ""
    phrase.gsub!(/[[:punct:]]/, '')
    phrase.gsub!(" ", "")
    phrase.downcase!
  end
  phrase
end

# Tests of palindrome function

phrase = "Madam, I'm Adam"
puts "phrase: #{phrase}"
puts "is pal?: #{is_pal?(phrase: phrase)}"
puts

phrase = "Walk, don't run"
puts "phrase: #{phrase}"
puts "is pal?: #{is_pal?(phrase: phrase)}"
puts

phrase = ""
puts "phrase: #{phrase}"
puts "is pal?: #{is_pal?(phrase: phrase)}"
puts

phrase = "Live not on evil"
puts "phrase: #{phrase}"
puts "is pal?: #{is_pal?(phrase: phrase)}"
puts