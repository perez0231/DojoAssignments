var mongoose = require('mongoose')



var NotesSchema = new mongoose.Schema({
  content: String,
}, {timestamps:true})

var Note = mongoose.model('Note', NotesSchema)
