$(document).ready(function() {

    $("#click").click(function() {
        alert('you are n0w leaving the page');
    });

    $("#hide").click(function() {
        $("#hideshow").hide();
    });

    $("#show").click(function() {
        $("#hideshow").show();
    });
    $("#toggle").click(function() {
        $("#toggletext").toggle("slow");
    });

    $("#up").click(function() {
        $("#slideupdown").slideUp("slow");
      });

    $("#down").click(function(){
      $("#slideupdown").slideDown("slow");

    });

    $("#in").click(function(){
      $("#faded").fadeIn("slow");

    });

    $("#out").click(function(){
      $("#faded").fadeOut("slow");

    });

    $("#addbut").click(function(){
      $("#addtext").addClass("newclass");

    });

    $("#beforebutt").click(function(){
      $("#before").before("Add text");

      });

      $("#appendbut").click(function(){
        $("#append").append("Add text");

        });

      $("#htmlbut").click(function(){
        $("#poop").html("<p>bullshit text</p>");

        });

        $("button").click(function(){
                $("input:text").val("Glenn perez");

                });


});
