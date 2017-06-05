# just excercsie

=begin
  ppop
  poop
=end
puts "hello"
puts "My"
puts "ninja"


print "myNinjas"


BEGIN {
  puts "This is a begin block"

}
END{
  puts "this is my end block"
  }

# just ex
x =5; y = 10; z = x + y
puts z


first_name= "dan"
last_name= "perez"


puts "your Name is " + first_name + " " + last_name

puts "First name is #{first_name} and last name is #{last_name}"
puts "First name is %s and last name is %s" % [first_name, last_name]


z=50
puts "Value of z is #{z}"
puts "Value of z is %d" %z


#two tabs  New line quotes in quotes
puts "\t\t I am \n 5'10\" tall"

x = puts "hello world"

puts x


x= "codingDojo"

puts x.length
puts x.capitalize
puts x.upcase
puts x.downcase
puts x[2]

puts x.include?("Dojo")

puts "this word has the word 'Dojo'" if x.include? "Dojo"

y ="John, charles, matt, joe"
z= ""
puts "z is empty" if z.empty?
puts y.split (",")

String.new("i am a new string instance")
