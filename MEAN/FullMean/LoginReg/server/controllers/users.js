var mongoose = require('mongoose');
mongoose.Promise = global.Promise;
var User = mongoose.model('User');

module.exports = {
  create: function(req, res){
    User.findOne({email:req.body.email})
    .then((user)=>{
      console.log("export create controllers", user)
      if(user){
        res.json({error:true, messages:"user already exists"})
      }
      else{
        User.create(req.body, function (err, user){
          console.log("usercreated")
          if (err){
            res.json({error:true, messages: err.errors.email.messages})
          }
          else { res.json({error:false, user:user})
        }
          })
      }
    })
    .catch((err)=>{
      console.log(err)
    })

    },

  success: function(req, res){
    User.find({}, function(err, users){
      if (err) {console.log(err)}
      res.json(users)
    })
  },
  login: function(req, res){
    User.findOne({email:req.body.email}, function (err, user){
      if(err){
        console.log(err)
      }
      else if(user){
        console.log('found user :)', user)
        var validPassword = user.validPassword(req.body.password)
        if (validPassword){
          res.json({login:true, user:user})
        }
        else{
          res.json({login:false, error:'Invalid password'})
        }
      }
      else{
        console.log('user not found')
        res.json({login:false, error: "email is not found!"})
      }
    })
  }
}
