$(document).ready(function() {




    $('img').click(function() {
        var catphoto = $(this).attr('data-alt-src');
        $(this).attr('src', catphoto);




    });



});
