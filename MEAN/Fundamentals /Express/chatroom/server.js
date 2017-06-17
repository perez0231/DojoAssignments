var express = require('express')
var app = express()
var path = require('path')
var users=[];
var history=[];
// app.use(express.static(path.join(__)))
app.set('views', path.join(__dirname, "./views"));
app.set('view engine', 'ejs');


app.get('/', function(req, res){
  res.render('index')
})
var server = app.listen(8000, function() {
 console.log("listening on port 8000");
});
var io = require ('socket.io')
io= io.listen(server);

io.sockets.on("connection", function(socket){
  console.log(socket.id)
  socket.on("Users_name_joined", function(data){

    users.push({id:socket.id, name:data.name})
    var namesarray= users.map(function(x){ return x.name

    })

    socket.emit("Users_name_joined", {curr :users[users.length-1], all_users:namesarray
    })

  })
  socket.on("send_message", function(data){
    var sender= users.find(function(x){
      return x.id ==data.sender
    })
    data.sender= sender.name;
    console.log(data)
    io.emit("send_message",data)
  })
  socket.on("disconnect", function(){
    var index = users.findIndex(function(x){
      return x.id ==socket.id
    })

    if(index>=0){
      users.splice(index, 1);
      var namesarray= users.map(function(x){ return x.name
      })
      io.emit("user_left", {users: namesarray
      })


    }


  })
})
