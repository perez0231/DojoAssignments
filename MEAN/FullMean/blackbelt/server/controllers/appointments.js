var mongoose = require('mongoose')
var Appointment = mongoose.model('Appointment');

module.exports = {

    index: function(req, res){
      Appointment.find({ }, function(err, appointments) {
        if (err) { console.log(err)}

        else{res.json(appointments)}


      })
    },


  create: function(req, res){
   var date = new Date(req.body.date)
   var today = new Date();
   if (date < today){
     res.json({error:true, messages:"Dates can only be in at future date."})
   }
   else{
     Appointment.create(req.body, function(err, appointment){
       if(err){
         console.log(err)

       }
       else{
         res.json(appointment)
       }
     })

   }


 },

 delete: function(req, res){
   var appt_id= req.params.id
   Appointment.remove({_id:req.params.id},function(err, appointment){
			if (err) {
				console.log(err)
			}
			else{
				res.json({appointment});
			}
   })
 }
}
