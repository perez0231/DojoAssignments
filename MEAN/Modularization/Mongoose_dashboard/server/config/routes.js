var mongoose = require('mongoose');
var Animal = mongoose.model('Animal');
var animal = require('../controllers/animals.js');

module.exports = function(app) {
  app.get('/', function(req, res){
    animal.home(req, res)
    })

  app.get('/animals/new', function(req, res){
    res.render('new')
  })

  app.post('/animals', function(req, res) {
    animal.create(req, res);
  });

  app.get('/animals/:id', function(req, res){
    animal.show(req, res);
  });

  app.get('/animals/edit/:id/', function(req, res){
      animal.edit(req, res);
    })
    app.post('/animals/:id', function(req, res) {
      animal.update(req, res);
  });

    app.post('/animals/destroy/:id', function(req, res){
      animal.delete(req, res)
    });





}
