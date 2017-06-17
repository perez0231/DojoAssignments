function fibinazi() {
  var prev = 0;
  var current = 1;
  var result = prev + current

  function nacci() {
    console.log(result)
    prev = current;
    current = result;
    result = prev + current;


  }
  return nacci
}
var fibcounter = fibinazi();
fibcounter()
fibcounter()
fibcounter()
fibcounter()
fibcounter()
fibcounter()
fibcounter()
fibcounter()
fibcounter()
fibcounter()
fibcounter()
