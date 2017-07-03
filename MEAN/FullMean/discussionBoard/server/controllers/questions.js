var mongoose = require('mongoose');
mongoose.Promise = global.Promise;
var Question = mongoose.model('Question');

module.exports = {

    create: function(req, res){
      Question.create(req.body, function(err, question){
        if(err){console.log(err)}

        else{
          console.log(question)
        res.json(question)

      }


    })
  },

    index: function(req, res){
      Question.find({}, function(err, question){
        if (err){console.log(err)}

        else{
          console.log(question)
          res.json(question)
        }
      })
    },
    show: function(req, res){
      Question.findOne({_id: req.params.id})
      .populate("answers")
      .exec(function(err, question){
        if(err){
          console.log(err)
        }
        else{
          res.json(question)
        }
      })
    }

    }
