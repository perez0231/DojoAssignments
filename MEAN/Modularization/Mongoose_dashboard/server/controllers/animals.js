var mongoose = require('mongoose');
var Animal = mongoose.model('Animal')

module.exports ={

    home: function(req, res){
      console.log("controller")
      Animal.find({}, function(err, animals){
        res.json(animals)
      })
    },
    // create: function(req, res){
    //   Animal.create(req.body, function(err){
    //     res.redirect('/')
    //   });
    // },
    show: function(req, res){
      Animal.find({'_id': req.params.id}, function(err, animal){
        res.json(animal)
      })
    },

    edit: function(req, res){
      Animal.find({'_id': req.params.id}, function(err, animal){
        res.json(animal);
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
