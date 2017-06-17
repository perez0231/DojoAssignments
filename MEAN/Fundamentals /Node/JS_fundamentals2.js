//Create a simple for loop that sums all the integers between x and y (inclusive). Have it console log the final sum.
sum = 0
function loopAdd(x,y){
  for (var x = x; x < y; x++){
    sum +=x;
  }
console.log(sum)

}
loopAdd(1,4)
//Write a loop that will go through an array, find the minimum value, and then return it

arr= [100,-20, 35, 1, 2, -2];
function minVal(arr){
  var min = arr[0];
  for(var i = 0; i < arr.length; i++){
    if (arr[i] < min){
      min= arr[i];
    }

    }

console.log(min)
}
minVal(arr)


//Write a loop that will go through an array, find the average of all of the values, and then return it
function avgVal(arr){
  sum= 0
  for(var i=0; i <arr.length; i++){
    sum +=arr[i]
  }
  console.log(sum/arr.length)
  return (sum/arr.length)
}

avgVal(arr)

var NewObject = {


  loopAdd: function(x,y){
    var sum = 0
    for (var x = x; x < y; x++){
      sum +=x;
    }
  return sum;
},

  minVal: function(arr){

    sum= 0
    for(var i=0; i <arr.length; i++){
      sum +=arr[i]
    }
    return (sum/arr.length)
  },
  avgVal: function(arr){
    var sum =0;
    for(var i =0; i < arr.length; i++){
      sum +=arr[i];
    }
    return (sum/arr.length)

  }
}
var person= {
  name: "jimmy Mixer",
  distance: 0,

say_name: function(){
  console.log(person.name)
  return this
},
say_something: function(){
  console.log(person.name +" says 'i am cool' ")
  return this
},
walk: function(){
  person.distance += 3
  console.log(person.name+ " is walking")
  return this
},
run: function(){
  person.distance += 10
  console.log(person.name+ " is running")
  return this
},

crawl: function(){
  person.distance +=1
  console.log(person.name+ " is crawling")
}

}

person.say_something().walk().run()
