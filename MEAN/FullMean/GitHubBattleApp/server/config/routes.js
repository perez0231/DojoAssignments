var mongoose = require('mongoose');
var User = mongoose.model('User');
var users = require('../controllers/users.js');

module.exports = function(app) {
  console.log('routes')
  app.get('/users', function(req, res){
    users.home(req, res)
    })

  app.get('/users/new', function(req, res){
    res.render('new')
  })

  app.post('/users', function(req, res) {
    console.log("hit it up post that controller")
    users.create(req, res);
  });

  app.get('/users/:id', function(req, res){
    users.show(req, res);
  });

  app.get('/users/edit/:id/', function(req, res){
      users.edit(req, res);
    })
  app.post('/users/:id', function(req, res) {
      users.update(req, res);
  });

  app.delete('/users/:id', function(req, res){
      users.delete(req, res)
    });





}
