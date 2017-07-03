var mongoose = require('mongoose');
var Note = mongoose.model('Note');
var notes = require('../controllers/notes.js');

module.exports = function(app) {
  console.log('routes')
  app.get('/notes', function(req, res){
    notes.home(req, res)
    })

  app.get('/notes/new', function(req, res){
    res.render('new')
  })

  app.post('/notes', function(req, res) {
    console.log("hit it up post that controller")
    notes.create(req, res);
  });

  app.get('/notes/:id', function(req, res){
    notes.show(req, res);
  });

  app.get('/notes/edit/:id/', function(req, res){
      notes.edit(req, res);
    })
  app.post('/notes/:id', function(req, res) {
      notes.update(req, res);
  });

  app.delete('/notes/:id', function(req, res){
      notes.delete(req, res)
    });





}
