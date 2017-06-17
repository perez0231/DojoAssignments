var mongoose = require('mongoose');
var Person = mongoose.model('Person');

module.exports={

  home: function(req, res){
    Person.find({}, function(err, person){
      res.json(person)
    })
  },

  create: function(req, res){
		var person = new Person({name: req.params.name})
		person.save(function(err){
			if(err) {
	      		console.log('something went wrong');
	    	}
	    	else {
	      		console.log('successfully added a person!');
	      		res.redirect('/');
		  	}
		})
	},
  delete: function(req, res){
    Person.findOne({'name': req.params.name}, function(err, person){
      if (person != null){
        person.remove()
      }
      res.redirect('/')
    })
  },
  show: function(req, res){
    Person.findOne({'name':req.params.name}, function(err, person){
      if (person==null){
        res.redirect('/')
      } else {res.json(person)}
    })
  }






}
