$(document).ready(function() {

    $(document).on('click', '.card', function() {
        $(this).children().toggle('slow');

    });

    $('form').submit(function() {

        var first = $('#fname').val();
        var last = $('#lname').val();
        var description = $('#desc').val();

        $('#fname').val('')
        $('#lname').val('')
        $('#desc').val('')

        console.log(description);


        $('.right').append("<div class=card><h2>" + first + " " + last + "</h2>,<h4> Click to add description</h4> <p hidden>" + description + "</p></div>");

        return false;

    });
});


// $(document).click(function() {
//
//
//     $('.right').append(`<h1 class="appendinfo">${first} ${last}</h1>`);
//     $('.right').append(`<p class="description app">${description}</p>`);
//
//
//     $(document).on('click', '.appendinfo', function() {
//       $(this).click(function() {
//  $(.children).toggle("slow");
