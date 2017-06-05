def new_user first_name: "first", last_name: "last"
  puts "Welcome to our site, #{first_name} #{last_name}!"
end
def new_user greeting="Welcome", first_name: "first", last_name: "last"
    puts "#{greeting}, #{first_name} #{last_name}"
end
our_user = {first_name: "Daniel", last_name: "Perez"}
#new_user                  # => Welcome, first last
new_user "Hello", our_user # => Hello, Oscar Vazquez


a = {first_name: "Michael", last_name: "Choi"}
b = {first_name: "John", last_name: "Doe"}
c = {first_name: "Jane", last_name: "Doe"}
d = {first_name: "James", last_name: "Smith"}
e = {first_name: "Jennifer", last_name: "Smith"}\

names = [a, b, c, d, e]

def new_users(names)
  for i in 0..names.length
  new_user "Hello", names[i]
end
end



new_user
