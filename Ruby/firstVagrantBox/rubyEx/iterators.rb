x = (1..5)

puts "class name: #{x.class}"
puts "there is a three!" if x.include? 3
puts "The last number of the range is" + x.last.to_s
puts "The Max number of this range is"+ x.max.to_s
puts "The minimum number of this range is " + x.min.to_s

y = ('a'..'z')
puts y.to_a.shuffle.to_s



def test
  puts "you are in the method"
  yield
  puts "you are back in the method"
  yield
end
test {puts "you are on the block wit yo bois"}


def test
  yield(5)
  puts "you are in the method test"
  yield (100)
end
test {|i| puts "you are in the block #{i}"}


def square num
  puts "num is #{num}"
  puts "yield (num) has a value of #{yield(num)}"
end

square(7) {|i| i*i}
