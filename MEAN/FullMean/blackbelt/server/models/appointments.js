console.log('Appoint Model');
var mongoose = require('mongoose');
var Schema = mongoose.Schema;

var AppointmentSchema = new mongoose.Schema({
	 date:{ type: Date, required: true},
	 time:{ type: String, required:true,
	 },
	complaint:{ type: String, required: true, minlength: 10 },
  user: String,
	_user:{ type: mongoose.Schema.Types.ObjectId, ref: "User" }
},{timestamps:true});

mongoose.model('Appointment',AppointmentSchema);
var Appointment = mongoose.model('Appointment');
