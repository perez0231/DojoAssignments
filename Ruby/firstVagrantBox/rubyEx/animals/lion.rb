require_relative 'mammals'
class Lion < Mammal
  def initialize
    @health =170
  end
  def fly
    @health -= 10
    self
  end

  def attack_town
    @health -= 50
    self
  end

  def eat_human
    @health += 20
    self
  end
end
daniel = Lion.new
daniel.display_health
daniel.attack_town.attack_town.attack_town.fly.eat_human.fly.display_health
