var mongoose = require('mongoose');

var AppointmentSchema = new mongoose.Schema({
  name: {type: String, minlength: 2, maxlength: 20,required: true},
  date: {type: Date, required: true},
  complain: String,
  time: {type: Date, required: true},
}, {timestamps: true})

var Appointment = mongoose.model('Appointment', AppointmentSchema);
