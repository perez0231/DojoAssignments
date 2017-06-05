a = {first_name: "Michael", last_name: "Choi"}
b = {first_name: "John", last_name: "Doe"}
c = {first_name: "Jane", last_name: "Doe"}
d = {first_name: "James", last_name: "Smith"}
e = {first_name: "Jennifer", last_name: "Smith"}
names = [a, b, c, d, e]

def new_users(names)
  puts "You have #{names.length} in your data"
  for i in 0...names.length
    puts "hello #{names[i][:first_name]} #{names[i][:last_name]}"
  end

end



new_users(names)
