var mongoose = require('mongoose')



var AnimalSchema = new mongoose.Schema({
  name: String,
  height: String,
  attack: String,
  special_ability: String
})

var Animal = mongoose.model('Animal', AnimalSchema)
