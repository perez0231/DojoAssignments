var users = require('../controllers/users.js');
module.exports = function(app) {
  app.get('/success', function(req, res) {
    console.log("coroutes")
    users.success(req, res);
  })
  app.post('/user', function(req,res){
    users.create(req, res);
  })
  app.post('/login', function(req, res){
    users.login(req, res);
  })
}
