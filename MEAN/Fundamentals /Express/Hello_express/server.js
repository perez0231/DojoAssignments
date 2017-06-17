var express = require("express")

var app = express();

app.get('/', function(request, response){
    response.send("hello Express")
})


app.listen(8000, function*(){
    console.log("on 8000")
})