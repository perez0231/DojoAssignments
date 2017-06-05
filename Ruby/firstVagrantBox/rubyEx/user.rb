class User
  attr_accessor :first_name, :last_name
  def initialize(f_name, l_name)
    @first_name = f_name
    @last_name = l_name
  end

def full_name
  puts "I am #{@first_name} #{@last_name}"
end

def sup_bro
  puts "Sup Bro.."
end
def self.foo
  puts "this is a class method"
end


end
daniel = User.new("Danny", "P")
puts daniel.first_name, daniel.last_name
daniel.full_name
daniel.sup_bro



class Myclass
  def some_method
    puts "my instance method"
  end
end
something =  Myclass.new
something.some_method


class CodingDojo
  @@no_of_branches = 0
  def initialize(id, name, address)
    @branch_id = id
    @branch_name = name
    @branch_address = address
    @@no_of_branches += 1
    puts "Created branch #{@@no_of_branches}"
  end
  def hello
    puts "Hello CodingDojo!"
  end
  def display_all
    puts "Branch ID: #{@branch_id}"
    puts "Branch Name: #{@branch_name}"
    puts "Branch Address: #{@branch_address}"
  end
end
# now using above class to create objects
dojoLoc1=CodingDojo.new(1,"DC", "McClean")
dojoLoc1.display_all
dojoLoc2=CodingDojo.new(2,"LA", "Whitter")
dojoLoc2.display_all
dojoLoc3=CodingDojo.new(100,"SF", "Berkeley")
dojoLoc3.display_all
puts DC.branch_name 
