var express = require("express");
// path module -- try to figure out where and why we use this
var path = require("path");
// create the express app
var app = express();
var bodyParser = require('body-parser');
// use it!
app.set('view engine', 'ejs');

app.use(bodyParser.urlencoded({ extended: true }));




// static content
app.use(express.static(path.join(__dirname, "./static")));

//setting up ejs and view folders
app.use(express.static(path.join(__dirname, "./views")))
app.set('view engine', 'ejs');

//root route to render the index.ejs view
app.get('/', function(req, res) {
 res.render("index");
})





// this selects our port and listens
// note that we're now storing our app.listen within
// a variable called server. this is important!!
var server = app.listen(8000, function() {
 console.log("listening on port 8000");
});
// this is a new line we're adding AFTER our server listener
// take special note how we're passing the server
// variable. unless we have the server variable, this line will not work!!
var io = require('socket.io').listen(server);
var count=0
// Whenever a connection event happens (the connection event is built in) run the following code
io.sockets.on('connection', function (socket){
  socket.on("updateCount", function (data){
    count++;
    console.log(count)
    io.emit('countUpdated', {response: count});
  })
  socket.on("reset_count", function (data){
        count = 0;
        console.log(count);
        io.emit('count_reset', {response: count});
})

})
