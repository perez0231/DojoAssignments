var mongoose = require('mongoose');
var Note = mongoose.model('Note')

module.exports ={

    home: function(req, res){
      console.log("controller")
      Note.find({}, function(err, notes){
        res.json(notes)
      })
    },
    create: function(req, res){
      console.log("here")
        Note.create(req.body, function(err){
          if(err){
            console.log(err)
          }
          else {
        res.redirect('/notes')
              console.log("post controller")
            }
        });
    },

    show: function(req, res){
      Note.find({'_id': req.params.id}, function(err, Note){
        res.json(Note)
      })
    },

    edit: function(req, res){
      Note.find({'_id': req.params.id}, function(err, Note){
        res.json(Note);
      });
    },

    // update: function(req, res){
    //   Animal.update({'_id':req.params.id}, req.body, function(err, animal){
    //     res.redirect('/animals/'+req.params.id)
    //   });
    // },
    // delete: function(req, res){
    //   Animal.deleteOne({'_id': req.params.id}, function(err){
    //     res.redirect('/')
    //   })
    //
    // }



}
