var mongoose = require('mongoose');
var User = mongoose.model('User');


module.exports ={


  login: function(req, res){
    User.findOne({ name: req.body.name}, function(err, user){
      console.log("controllers login")
      console.log(req.body.name)
      if(err){res.json(err)}

      else if(!user){
          console.log("noUser")
          User.create({name:req.body.name}, function(err, user){
            console.log(req.body.name)
          if(err){
            res.json(err);
          }
          else{
            res.json(user)
          }
        })
      }
      else{
        res.json(user)
      }
    })
  }

}
