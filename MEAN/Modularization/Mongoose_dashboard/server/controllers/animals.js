var mongoose = require('mongoose');
var Animal = mongoose.model('Animal')

module.exports ={

    home: function(req, res){
      Animal.find({}, function(err, animals){
        res.render('index', {animals})
      })
    },
    create: function(req, res){
      Animal.create(req.body, function(err){
        res.redirect('/')
      });
    },
    show: function(req, res){
      Animal.find({'_id': req.params.id}, function(err, animal){
        res.render('animal', {animal})
      })
    },

    edit: function(req, res){
      Animal.find({'_id': req.params.id}, function(err, animal){
        res.render('edit_animal', {animal});
      });
    },

    update: function(req, res){
      Animal.update({'_id':req.params.id}, req.body, function(err, animal){
        res.redirect('/animals/'+req.params.id)
      });
    },
    delete: function(req, res){
      Animal.deleteOne({'_id': req.params.id}, function(err){
        res.redirect('/')
      })

    }



}
