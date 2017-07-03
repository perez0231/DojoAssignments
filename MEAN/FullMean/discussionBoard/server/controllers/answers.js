var mongoose = require('mongoose');
mongoose.Promise = global.Promise;
var Question = mongoose.model('Question');
var Answer = mongoose.model('Answer');
module.exports = {

  create: function(req, res){
    var question_id = req.params.id

    Question.findOne({_id: question_id}, function(err, question){
      var answer = new Answer(req.body)
        answer._question = question_id
        answer.save(function (err){
          question.answers.push(answer)
          question.save(function(err, question){
            if(err){
              console.log(err)
            }
            else{
              res.json(question)
            }

          })
        })
    })




  },

  like: function(req, res){
    var answer_id = req.params.id
    Answer.findOne({_id: answer_id}, function(err, answer){
      answer.like(function(err){
        if (err){
          console.log(err)
        }
        else{
          res.json(answer)
        }
      })
    })
  }





}
