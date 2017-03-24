
$(document).ready(function(){
.alert("alert")
  $('img').click(function(){
      $.get("http://anapioficeandfire.com/api/houses/",function(res){
        console.log(res);

      },"json");
    });



});








  //   $('#wrapper').append('<img src="http://pokeapi.co/media/img/' + i +'.png">')
  //
  // $.get(document).ready(function() {




});
