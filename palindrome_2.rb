# Create recursive function is_pal? to test if phrase is palindrome

# Check if phrase is palindrome
#   First time, format string to remove punctuation and whitespace
# @param [String] phrase may include whitespace and punctuation
# @param [Boolean] strip true = format string to strip punctuation, whitespad
#                        false = string already formatted
# @return [Boolean] true = is palindrome, false = not palindrome
def is_pal?(phrase:, strip: false)
  phrase = strip_string(phrase: phrase) if strip
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

def print_palindromes(filename)
  f = File.open(filename, 'r') do |f|
    f.each_line do |line|
      line = line.rstrip
      save_line = String.new(line)
      if is_pal?(phrase: line, strip: true)
        puts
        puts "#{save_line}"
      end
    end
  end
end

# Tests of palindrome function

print_palindromes("phrases.txt")