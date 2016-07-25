# convert number in base 10 to string in specified base
def conv_num(num, base)
  new_base_num = ""
  while num > 0
    new_base_num = new_base_num.prepend((num % base).to_s)
    num = (num / base)
  end
  return new_base_num
end

num = 45
base = 3
result = conv_num(num, base)
puts "num, base, result: #{num}, #{base}, #{result}"

base = 10
result = conv_num(num, base)
puts
puts "num, base, result: #{num}, #{base}, #{result}"