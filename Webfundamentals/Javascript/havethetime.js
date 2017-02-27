
function time(HOUR, MIN, PERIOD) {


  if (MIN > 30) {
  MIN= "Its almost";
  HOUR = HOUR +1;
} else {
      MIN = "Its just after"
}


if (PERIOD = "AM"){
  PERIOD= "in the morning"
}
if(PERIOD = "PM"){

 PERIOD="in the the evening"
}

console.log(MIN, HOUR, PERIOD);


}

time(9, 50, "PM");
