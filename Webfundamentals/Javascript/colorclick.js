function random_color()
{
   var rgb = ['a','b','c','d','e','f','0','1','2','3','4','5','6','7','8','9'];
   color = '#'  //this is what we'll return!
   for(var i = 0; i < 6; i++)
   {
      x = Math.floor((Math.rando m()*16))
      color += rgb[x];
   }
   return color;
}

$(document).ready(function(){

   $('#large_box').click(function(){
     $(this).children().css('background', random_color)
     $(this).css('background', random_color)
   });

   $('.side_box').click(function(event){
     $(this).children().css('background-color', random_color);
   });
   $('.middle_box').click(function(event){
     $(this).parent().css('background-color', random_color);

});
});
