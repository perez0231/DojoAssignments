var mongoose = require('mongoose')
var User = mongoose.model('User')

module.exports = {
  home: function(req, res){
        console.log("controller")
        User.find({}, function(err, user){
          res.json(user)
        })

},

create: function(req, res){
      console.log("here")


      User.findOne({login: req.body.login}, function(err, user){
        if (user){
          return res.json(user)
        }
        else{
          User.create(req.body, function(err, user){
            if(err){console.log(err)}
            else {
              res.status(201).json(user)
                console.log(user)
                console.log(req.body)
                console.log("post controller")
              }
          })



        }

      })

    },
}
