var express = require("express");
var path = require("path");
// create the express app
var app = express();
// require bodyParser since we need to handle post data for adding a user
var bodyParser = require("body-parser");
app.use(bodyParser.urlencoded({ extended: true }));
// static content

// app.use(bodyParser.urlencoded({ extended: true }));

app.use(express.static(path.join(__dirname, "./MEAN-demo/dist")));
// setting up ejs and our views folder
// app.set('views', path.join(__dirname, './client/views'));
app.set('view engine', 'ejs');

require('./server/config/mongoose.js');
//routes-
var routes_setter = require('./server/config/routes.js');
routes_setter(app);

app.get('*', function(req, res){
  res.sendfile(path.resolve("./dist/index.html"))
})

app.listen(8000, function() {
  console.log("listening on port 8000");
})
