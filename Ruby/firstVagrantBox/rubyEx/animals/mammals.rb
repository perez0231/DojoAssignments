puts 'I am in the mammal file'


class Mammal
  def initialize
    @health= 170
  end

  def display_health
    puts @health
  end

  def eat
    puts "eating food"
  end
  def drink
    puts "drinking water"
  end

  def calling_cry
    calling_cry
  end

  private
  def cry
    puts "Sniff, crying"
  end


  def calling_speak
    speak
  end
  def speak
    puts "This is a protected Method"
  end
end
