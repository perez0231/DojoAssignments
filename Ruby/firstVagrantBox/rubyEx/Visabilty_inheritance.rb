#all method in ruby classes are public
#3 methods public, protected, and private
  #public - methods that can be called within the class, subclasses and instances without restriction.
  #protected -  methods that can only be called within the class and subclasses either explicitly or implicitly
  #private-  methods that can only be called within the class and subclasses implicitly


  #A class can inherit methods from parent class. When a class inherits from a parent class, it is called a child class or subclass.

class Mammal


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
class Human < Mammal
  def explicitily_cry
    self.cry
  end

  def implicitily_cry
    cry
  end

  def subclass_method
    drink
  end
def explicitly_speak
  self.speak
end
def implicitly_speak
  speak
end
def another_method
  self.eat
end
end

marco= Human.new
marco.cry
marco.explicitily_cry
marco.implicitly_cry
#marco.another_method
#marco.subclass_method
#marco.speak
#marco.explicitly_speak
#marco.implicitly_speak
dog=Mammal.new
mammal.calling_cry
mammal.cry
mammal.speak
mammal.calling_speak
