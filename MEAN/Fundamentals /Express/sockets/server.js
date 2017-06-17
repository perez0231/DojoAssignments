var express = require("express");
// path module -- try to figure out where and why we use this
var path = require("path");
// create the express app
var app = express();
var bodyParser = require('body-parser');
// use it!
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

//post route that will add a user
app.post('/result', function(req,res){
  console.log("post data", req.body);

  res.render('results', {info: req.body})
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

// Whenever a connection event happens (the connection event is built in) run the following code
io.sockets.on('connection', function (socket) {
  console.log("WE ARE USING SOCKETS!");
  console.log(socket.id);
  //all the socket code goes in here!
  socket.on("button_clicked", function (data){
      console.log('Someone clicked a button!  Reason: ' + data.reason);
      socket.emit('server_response', {response: "sockets are the best!"});
  })

})
