class Fixnum
  def identify
    puts self
  end

end
class String
  def identify
    puts self
  end
end

2.identify
3.identify

"string".identify
"helloWord".identify

class Mammal
  def initialize
    puts "I am Alive"
  end
  def breathe
    puts "I am breathing"
    self
  end
  def identify
    puts self
    self
  end
end
dog=Mammal.new.identify.breathe
dog.identify
dog.identify.breathe
