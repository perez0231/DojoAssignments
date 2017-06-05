require_relative 'humans'

class Wizard < Human
  # your code here
def initialize
  super
  @health =50
  @itelligence=25
end

def heal
  @health +=10
  self
end

def fireball(obj)
  obj.health -=20
end
