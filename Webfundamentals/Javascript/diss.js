$(document).ready(function() {

    $('.ninja').click(function() {
        $(this).hide('slow');
    });

    $('#restbut').click(function() {
        $(".ninja").show('slow');
    });

    $(document).on("click", 'img', function() {
        $(this).hide('slow');

    });


    $("#startbut").click(function() {
for (var i= 0;  i < 5; i++){
  $(".ninjadiv").append('<img class ="ninja" src="ninja.png" alt="Ninja" height="300px">');
}



    });





});
