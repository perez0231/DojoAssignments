
x = [3,5,"Dojo", "rocks", "Michael", "Sensei"]
// for (var i= 0; i < x.length; i++){
// console.log(x[i])
// }

for (index in x){

  console.log(x[index])
}

x.push(100)
console.log(x)


x=["jello", "world", "JS is fun"]
console.log(x)

var sum=0;
for(var i = 0; i < 501; i++){
  sum += i;

}
console.log(sum)


arr= [1, 5, 90, 25, -3, 0]
var min = arr[0]

for(var i = 0; i < arr.length; i++){
  if(min > arr[i]){
     min = arr[i]

  }
}
console.log(min)
var sum = 0
for(var i = 0; i < arr.length; i++){
  sum += arr[i]


}
console.log(sum/arr.length-1)


var newNinja = {
 name: 'Jessica',
 profession: 'coder',
 favorite_language: 'JavaScript', //like that's even a question!
 dojo: 'Dallas'
}


for(key in newNinja){
  console.log(key, newNinja[key])
}

console.log(first_variable);
var first_variable = "Yipee I was first!";
function firstFunc() {
  first_variable = "Not anymore!!!";
  console.log(first_variable);
}
console.log(first_variable);
