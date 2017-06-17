module.exports = function(){
return {
add: function(num, num2){
  console.log("the sum is:", num + num2);
},
multiply: function(num, num2){
  console.log("the total is:", num * num2);
},

square: function(num){
  console.log("total is:", num * num)
},
random: function(num, num2){
 console.log(Math.floor(Math.random() * num2) + num)  
}


}

}
