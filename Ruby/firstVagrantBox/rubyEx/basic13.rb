def printnum
  for i in 1..256
    puts i
  end
end


def printodd
  for i in 1..255
    if i% 2 != 0
      puts i
    end
  end
end

def printsum
  sum= 0
  for i in 1..255
    puts i
    puts sum += i
  end
end



def array(arr)
  arr.each {|arr| puts arr}
end

def max(arr)
  puts arr.max
end

def avg(arr)
  sum = 0
  for i in arr
    sum += i
  end
  puts sum.to_f/arr.length.to_f

end

def one_odd_array
  arr=[]
  for i in 1..256
    if i %2 !=0
      arr.push(i)
    end
  end
  puts arr
end

def greater_than_y(arr, y)
  for i in arr
    if i < y
      arr.delete(i)
    end
  end
puts arr
end

def square_values(arr)
  arr.each {|arr| puts arr * arr}
end

def delete_negitives(arr)
  for i in 0...arr.length
    if arr[i] < 0
      arr[i] = 0
    end
  end
  puts arr
end


def max_min_avg(arr)
  puts arr.max
  puts arr.min
  sum = 0
  for i in arr
    sum += i
  end
  puts sum.to_f/arr.length.to_f
end

def shift(arr)
  for i in 0...arr.length
    arr[i]= arr[i +1]
    if arr[i] == nil
      arr[i]=0
    end
  end
  print arr
end



def num_to_string(arr)
  for i in 0...arr.length
    if arr[i]< 0
      arr[i]="Dojo"
    end
  end
  print arr
end













#puts printnum
#puts printodd
#puts printsum
#array([1,3,5,7,9,13])
#max([1,3,5,7,9,100])
#avg([1,3,5,7,9,100])
#one_odd_array
#greater_than_y([1, 3, 5, 7], 3)
#square_values([1, 3, 5, 7])
#delete_negitives [1, 5, 10, -2]
#max_min_avg ([1,3,5,7,9,100])
#shift([1, 5, 10, 7, -2])
num_to_string [-1,-2, 3, 5, -9, 10]
