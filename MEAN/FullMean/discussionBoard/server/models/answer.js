var mongoose = require('mongoose');

var AnswerSchema = new mongoose.Schema({
  _question: [{type: mongoose.Schema.Types.ObjectId, ref: 'Question'}],
  answer: { type: String, required: true, minlength: 5 },
  details:String,
  user: String,
  likes:{
    type: Number,
    default:0
  }

}, {timestamps: true})

AnswerSchema.methods.like = function(callback){
  this.likes += 1;
  this.save(function(err){
    callback(err)
  });
};

var Answer = mongoose.model('Answer', AnswerSchema);
