var express =require ('express')
var path = require('path')
var app = express()
var mongoose = require('mongoose')

mongoose.connect('mongodb://localhost/mongoose_db')

mongoose.Promise = global.Promise

var AnimalSchema = new mongoose.Schema({
  name: String,
  height: String,
  attack: String,
  special_ability: String
})


mongoose.model('Animal', AnimalSchema)

var Animal = mongoose.model('Animal')

var bodyParser = require('body-parser');

app.use(bodyParser.urlencoded({
  extended: true
}));


app.use(express.static(path.join(__dirname, './static')));
// Setting our Views Folder Directory
app.set('views', path.join(__dirname, './views'));
// Setting our View Engine set to EJS
app.set('view engine', 'ejs');

app.get('/', function(req, res) {
  Animal.find({}, function(err, animals){
    res.render('index', {animals})
  })

})
app.get('/animals/new', function(req, res){
  res.render('new')
})

app.post('/animals', function(req, res) {
  console.log("POST DATA", req.body);
  Animal.create(req.body, function(err){
    if(err){ console.log(err)}
    res.redirect('/')
  });
})

app.get('/animals/:id', function(req, res){
  Animal.find({'_id': req.params.id}, function(err, animal){
    res.render('animal', {animal})
    console.log(animal)

  })


})





  app.get('/animals/edit/:id/', function(req, res){
    Animal.find({'_id':req.params.id}, function(err, animal){
      res.render('edit_animal', {animal});

    })
  })
  app.post('/animals/:id', function(req, res) {
    Animal.update({ _id: req.params.id }, req.body, function(err, animal) {
        res.redirect('/animals/' + req.params.id)
    })
});

  app.post('/animals/destroy/:id', function(req, res){
    Animal.deleteOne({'_id': req.params.id}, function(err){
      res.redirect('/')
    })
  })


app.listen(8000, function() {
  console.log("listening on port 8000");
})
