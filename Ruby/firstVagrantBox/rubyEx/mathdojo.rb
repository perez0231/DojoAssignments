class MathDojo
  # your code here
  def initialize
    @sum = 0
  end

  def add(*num)
    @sum += num.flatten.reduce(0, :+)
    self
  end
def sub(*num)
  @sum -= num.flatten.reduce(0, :+)
  self
  end

def result
  puts @sum
  end


end

challenge1 = MathDojo.new.add(2).add(5, 1).sub(2).result # => 4
challenge2 = MathDojo.new.add(1).add([3, 5, 7, 8], [2, 4.3, 1.25]).sub([2,3], [1.1, 2.3]).result
#challenge2 = MathDojo.new.add(1).add([3, 5, 7, 8], [2, 4.3, 1.25]).subtract([2,3], [1.1, 2.3]).result # => 23.15
