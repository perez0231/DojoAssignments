
var mongoose = require('mongoose');

var CommentSchema = new mongoose.Schema({
  user: { type: String, required: true},
  comment: { type: String, required: true },
  _post: {type: mongoose.Schema.Types.ObjectId, ref: 'Message'},
}, {timestamps: true})

var Comment = mongoose.model('Comment', CommentSchema); 
