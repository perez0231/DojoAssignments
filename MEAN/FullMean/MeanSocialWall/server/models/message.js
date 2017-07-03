var mongoose = require('mongoose');

var MessageSchema = new mongoose.Schema({
 user: { type: String, required: true},
 message: { type: String, required: true },
 comments: [{type: mongoose.Schema.Types.ObjectId, ref: 'Comment'}],
}, {timestamps: true})

var Message = mongoose.model('Message', MessageSchema); 
