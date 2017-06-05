def puzzle1(arr)
  sum=0
    for i in 0...arr.length
      sum += arr[i]

    end
  puts sum
  p arr.reject{|arr| arr <10}

end

def puzzle2(arr)
  puts arr.shuffle
  p arr.reject{|arr| arr.length <5}

end

def puzzle3(arr)
  puts arr.shuffle.last
  first= arr.shuffle.first
  puts first
  if first == "a" or first == "e" or first == "i" or first == "o" or first == "u"
    puts "this is a vowel"
  end

end

def puzzle4()
  arr=[]
  for i in 0..10
    arr.push(rand(55..100))
  end
  p arr
end

def puzzle5()
  arr=[]
  for i in 0..10
    arr.push(rand(55..100))
  end
  p arr.sort
  p arr.min
  p arr.max

end

def puzzle6
  str= ""
  for i in 0..5
    str[i]=(65+rand(26)).chr
  end
  p str
end

def puzzle7
  arr= []
  for i in 0..9
    str =""
    for i in 0..4
      str[i]=(65+rand(26)).chr
    end
    arr.insert(0, str)
  end
  p arr
end
#puzzle1([3,5,1,2,7,9,8,13,25,32])
#puzzle2(["John", "KB", "Oliver", "Cory", "Matthew", "Christopher"])
#puzzle3(["a",'b',"c","d","e",'f',"g","h","i",'j','k',"l",'m',"n","o","p","q","r","s","t", "u", "v","w","x","y","z"])
#puzzle4
#puzzle5
#puzzle6
puzzle7
