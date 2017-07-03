console.log('User Model')
var mongoose = require('mongoose');
var Schema = mongoose.Schema;

var UserSchema = new mongoose.Schema({
        name: {
          type: String,
          required: "Need a User name.",
          maxlength: 20
        },
        appointment: [{
        	type: Schema.Types.ObjectId, ref: 'Appointment'
        }]
},{timestamps:true});


mongoose.model('User', UserSchema);
var User = mongoose.model('User');
