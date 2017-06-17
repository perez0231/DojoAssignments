var express = require('express')

var path = require('path')

var app = express();

var mongoose = require('mongoose')

mongoose.connect('mongodb://localhost/quotes_db');

mongoose.Promise = global.Promise;


var QuoteSchema = new mongoose.Schema({
  name: String,
  quote: String
})


mongoose.model('Quote', QuoteSchema)

var Quote = mongoose.model('Quote')


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
  res.render('index')
})
app.post('/submitQuotes', function(req, res) {
  console.log("POST DATA", req.body);
  Quote.create(req.body, function(err){
    if(err){ console.log(err)}
    res.redirect('quotes')
  });


});

app.get('/quotes', function(req, res) {
  Quote.find({}, function(err, quote) {
    if (err) {
      console.log(error);
    }
    res.render('quotes', {quote});
  })
})
app.listen(8000, function() {
  console.log("listening on port 8000");
})
