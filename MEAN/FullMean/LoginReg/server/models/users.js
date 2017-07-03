var mongoose = require('mongoose');
var bcrypt = require('bcrypt');
mongoose.Promise = global.Promise;

var UsersSchema = new mongoose.Schema({
  first_name: {type: String, required: true},
  last_name: { type: String, required: true},
  email: {type: String, required: true, unique: true,
    validate:{
      validator: function(value){
        return /^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$/.test( value )
      },
      message: "Incorrect email format"
  }
},
password: {type: String, required: true, minlength:8},
birthday: {type: Date, required: true}
}, {timestamps: true})

UsersSchema.methods.generateHash = function (password){
  return bcrypt.hashSync(password, bcrypt.genSaltSync(8))
};
UsersSchema.methods.validPassword= function(password){
  return bcrypt.compareSync(password, this.password);
};

UsersSchema.pre('save', function(done){
  this.password =this.generateHash(this.password)
  done()
});
var User = mongoose.model('User', UsersSchema)
