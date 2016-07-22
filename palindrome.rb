# Create recursive function to test if phrase is palindrome

# Check if phrase is palindrome
#   First, format string to remove punctuation and whitespace
# @param  String phrase includes whitespace and punctuation
# @return Boolean true = is palindrome, false = not palindrome
def is_pal?(phrase)
  phrase = strip_string(phrase)
  is_palindrome?(phrase)
end

# Strip string of punctuation and whitespace
# @param  String unformatted string
# @return String
def strip_string(phrase)
  unless phrase == ""
    phrase.gsub!(/[[:punct:]]/, '')
    phrase.gsub!(" ", "").downcase!
  end
  phrase
end

def is_palindrome?(phrase)
  return true if phrase.length <= 1
  return false unless phrase[0] == phrase[-1]
  is_palindrome?(phrase[1..-2])
end

phrase = "Madam, I'm Adam"
pal = is_pal?(phrase)
puts "phrase, pal: #{ phrase }, #{ pal }"

phrase = ""
pal = is_pal?(phrase)
puts "phrase, pal: #{ phrase }, #{ pal }"

phrase = "Walk, don't run"
pal = is_pal?(phrase)
puts "phrase, pal: #{ phrase }, #{ pal }"

phrase = "Live not on evil"
pal = is_pal?(phrase)
puts "phrase, pal: #{ phrase }, #{ pal }"
