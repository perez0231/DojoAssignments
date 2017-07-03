var mongoose = require('mongoose') //require mongoose for db

var UsersSchema = new mongoose.Schema ({
  login: {type:String, required:true, minlength:3},
  score: {type: Number},
  img: {type:String}
}, {timestamps:true})

var User= mongoose.model('User', UsersSchema)
