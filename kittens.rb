
require 'open-uri'
require 'json'

def display_kitten
  # use link from CodeAcademy exercise
  kittens = open('http://placekitten.com/')
  response_status = kittens.status
  response_body = kittens.read[559, 441]

  puts response_status
  puts response_body
end

def json_practice
  # Convert json to hash and print both
  value_json = '{"val":"test","val1":"test1","val2":"test2"}'
  value_hash = JSON.parse(value_json)
  puts "value_json: #{value_json}"
  puts "value_hash: #{value_hash}"

  #convert hash to json and print both
  my_hash = {dog: "poodle",
             cat: "siamese",
             bird: "robin"
             }
  my_json = my_hash.to_json
  puts "my_hash: #{my_hash}"
  puts "my_json: #{my_json}"
end

display_kitten
json_practice