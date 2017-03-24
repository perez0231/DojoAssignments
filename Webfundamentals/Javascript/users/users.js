$(document).ready(function() {
  // alert('hello!');
  // $('form').submit(function(){
  $('#but').click(function(){
    var fname= $('#fname').val()
    var lname= $('#lname').val()
    var email= $('#email').val()
    var phone= $('#phone').val()

    $('#table').append(
      `<tr><td>${fname}</td><td>${lname}</td><td>${email}</td><td>${phone}</td>`
    );


  });
  });
