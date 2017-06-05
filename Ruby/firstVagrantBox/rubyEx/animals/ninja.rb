require_relative 'humans'
class Ninja < Human
  # your code here

  def initialize
    super
    @stealth= 175
  end


  def steal(obj)
    attack(obj)
    @health+=10
  end

  def get_away
    @health -= 15
  end
  #def attack(obj)
  #  super
  #end
end
daniel =Ninja.new
puts daniel.health
dorian=Ninja.new
puts daniel.steal(dorian)
