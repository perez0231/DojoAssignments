var first_variable
function firstFunc() {
  first_variable = "Not anymore!!!";
  console.log(first_variable);
}

console.log(first_variable);
var first_variable = "Yipee I was first!";

console.log(first_variable);


// Problem #1 Solution
// functions and variable declarations hoisted to the top!
// Everything else left in the original order.
// firstFunc was never invoked, so first_variable after it was set to "Yipee I was first" remains "Yipee I was first".
// */
var food
function eat() {
  var food
  food = "half-chicken";
  console.log(food);
  var food = "gone";       // CAREFUL!
  console.log(food);
}
food="Chicken";
eat();
console.log(food);



var new_word;
function lastFunc() {
  new_word = "old";
  console.log(new_word)
}
new_word = "NEW!";
console.log(new_word);
