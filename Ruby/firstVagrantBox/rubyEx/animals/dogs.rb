puts 'I am in the dog file'
require_relative 'mammals'

class Dog < Mammal
def pet
  @health += 5
  self
end
def walk
  @health -=1
  self
end

def run
  @health-=10
  self
end
end
shadow=Dog.new
shadow.display_health
shadow.walk.walk.run.run.pet.display_health
