var mongoose = require('mongoose')
var Person = mongoose.model('Person')
var person = require ('../controllers/person.js')


module.exports= function(app){
  app.get('/', function(req, res){
    person.home(req, res);
  })

  app.get('/new/:name', function(req, res) {
        person.create(req, res);
    })
    app.get('/remove/:name', function(req, res) {
        person.delete(req, res);
    })

    app.get('/:name', function(req, res) {
        person.show(req, res);
    })





}
