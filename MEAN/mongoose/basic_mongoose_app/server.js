// Require the Express Module
var express = require('express');
// Create an Express App


var path = require('path');
// Setting our Static Folder Directory
var app = express();

var mongoose = require('mongoose');
// Require body-parser (to receive post data from clients)
// This is how we connect to the mongodb database using mongoose -- "basic_mongoose" is the name of
//   our db in mongodb -- this should match the name of the db you are going to use for your project.
mongoose.connect('mongodb://localhost/basic_mongoose_app');
mongoose.Promise = global.Promise;

var UserSchema = new mongoose.Schema({
  name:String,
  age:Number
})

mongoose.model('User', UserSchema);// We are setting this Schema in our Models as 'User', taking blueprint by making a new schema instance from mongoose.schema() object constructor.
var User= mongoose.model('User')  // We are retrieving this Schema from our Models, named 'User'

var bodyParser = require('body-parser');
// Integrate body-parser with our App
app.use(bodyParser.urlencoded({ extended: true }));
// Require path

app.use(express.static(path.join(__dirname, './static')));
// Setting our Views Folder Directory
app.set('views', path.join(__dirname, './views'));
// Setting our View Engine set to EJS
app.set('view engine', 'ejs');
// Routes
// Root Request



app.get('/', function(req, res) {
    User.find({}, function(err, users){
    });
    if(err){
      console.log("error")
    } else {
      res.render('index', {users});
    }
})


// Add User Request
app.post('/users', function(req, res) {
    console.log("POST DATA", req.body);
    var user = new User({name: req.body.name, age: req.body.age});
    // Try to save that new user to the database (this is the method that actually inserts into the db) and run a callback function with an error (if any) from the operation.
    user.save(function(err) {
        if(err){
          console.log("something went wrong");
        }
        else {
          console.log("user added succesfully");
          res.redirect('/');
        }
    // This is where we would add the user from req.body to the database.
})
})
// This is the route that we already have in our server.js
// When the user presses the submit button on index.ejs it should send a post request to '/users'.  In
//  this route we should add the user to the database and then redirect to the root route (index view).


// Setting our Server to Listen on Port: 8000
app.listen(8000, function() {
    console.log("listening on port 8000");
})
