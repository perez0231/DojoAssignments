$(document).ready(function() {
    $('form').submit(function() {
        var city = $('#city').val();
        console.log(city)
         $.get("http://api.openweathermap.org/data/2.5/weather?q=" + city + "&units=imperial&appid=7c0089a51d3a0058b9370a6f54a82ce1", function(res) {
            console.log(res)
              $('#cityinfo').html("<h4>City</h4>"+res.name);
              $('#poop').html("<h4>Temp</h4>" + res.main.temp);
        }, 'json');
        return false;
    });
});
