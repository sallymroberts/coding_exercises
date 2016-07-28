require 'rest-client'
require 'json'

url = 'https://api.spotify.com/v1/search?type=artist&q=tycho'
response = RestClient.get(url)
response_arr = JSON.parse(response)

response_arr.each do |elem|
  elem[1].each do |k, v|
    puts
    puts k
    puts v.class
  end
end

# puts response_arr[1]

# response_hash[1][:items].each do |elem|
#   puts elem
# end