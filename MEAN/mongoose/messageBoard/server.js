// Require the Express Module
var express = require('express');
// Create an Express App
var path = require('path');
// Setting our Static Folder Directory
var app = express();
var mongoose = require('mongoose');
//connect to our DB!
mongoose.connect('mongodb://localhost/messageBoard');
var bodyParser = require('body-parser');
// Integrate body-parser with our App
app.use(bodyParser.urlencoded({ extended: true }));
// Require path
app.use(express.static(path.join(__dirname, './static')));
// Setting our Views Folder Directory
app.set('views', path.join(__dirname, './views'));
// Setting our View Engine set to EJS
app.set('view engine', 'ejs');

//similar to callbacks, have something happen and then do something else. chain actions, callbacks vs Promises
mongoose.Promise = global.Promise;

//create schema variable
var Schema =mongoose.Schema;
//create message schema

var messageSchema = new mongoose.Schema({
  name:{type: String, required:true, minlength:4},
  content: {type: String, required:true},
  comments: [{type: Schema.Types.ObjectId, ref:"Comment"}] //refercences to objects
},{timestamps:true});

var commentSchema= new mongoose.Schema({
  _message: {type: Schema.Types.ObjectId, ref: 'Message'},
  name:{type:String, required:true, minlength:4},
   content: { type: String, required: true },
  }, {timestamps: true });

  //register models
  var Message= mongoose.model('Message', messageSchema);
  var Comment = mongoose.model('Comment', commentSchema);

//routes
app.get('/', function(req, res){
  Message.find({})
  .populate('comments')
  .exec(function(err, results){
    if(err){console.log(err)}
      console.log(results)
      res.render('index',{messages:results})

  });

});

app.post('/messages', function(req, res){
  Message.create(req.body, function(err, result){
    if (err){console.log(err);
      res.redirect('/');
    }
  })
})
app.post('/messages/:id/comments', function(req,res){
  //find messge comment will belong to
  Message.findOne({_id: req.params.id}, function(err, message){
    ///create a comment using data from form
    var comment = new Comment(req.body);
    ///establish a relationship; message.id fed into this function after being found
    comment._message= message._id
    // comment now belongs to ^ found message. save both to DB
    comment.save(function(err){
      //push comment into message_comment arry if no errs
        message.comments.push(comment);
        // save updated message
        message.save(function(err){
          if (err){console.log(err)}
          else{res.redirect('/')}
        })
    });
  });
});

app.listen(8000, function() {
    console.log("listening on port 8000");
});
