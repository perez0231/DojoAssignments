$(document).ready(function() {


        for(var i = 1; i <151; i++){
            $('.pokemon').append('<img id=' + i + ' src="http://pokeapi.co/media/img/' + i + '.png">')
}
        $(document).on('click', 'img', function(){
//
            var id = $(this).attr('id');
            $.get("http://pokeapi.co/api/v1/pokemon/" + id + "/", function(res){
                $('.name').html(res.name);

                var htmlstr = "";
                htmlstr += "<h4>Types</h4>";
                htmlstr += "<ul>";
                for (var i = 0; i <res.types.length; i++){
                  htmlstr += "<li>" + res.types[i].name + "</li>"
                }
                htmlstr += "</ul>";

                $(".type").html(htmlstr);
                $(".weight").html("<h4>Weight</h4>" + res.weight);



    }, "json");


});









});
