class Apple
  attr_accessor :color

  def initialize(color)
    @color= color
  end
end



myApple=Apple.new "red"
puts myApple.color
