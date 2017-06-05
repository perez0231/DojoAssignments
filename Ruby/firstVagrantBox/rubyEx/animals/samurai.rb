require_relative 'humans'
require_relative 'ninja'



class Samurai < Human
  # your code here
@@total_sams =0

  def initialize
    super
    @health =200
    @@total_sams +=1
  end


  def self.total_sams
    puts @@total_sams

  end

  def death_blow(obj)
    obj.health =0
  end

  def meditate
    @health =200
  end

end



daniel=Samurai.new
luis=Ninja.new
dorian=Samurai.new
daniel.death_blow(dorian)
puts dorian.health
puts "Ninja #{luis.health}"
Samurai.total_sams
