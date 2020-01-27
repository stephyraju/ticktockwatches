$(document).ready(function() {
    // messages timeout for 10 sec 
    setTimeout(function() {
        $('.messages').fadeOut('slow');
    }, 4000);
});

// Search icon display
function myFunction() {

 var x = document.getElementById("searchDiv");
  if (x.style.display === "none") {
    x.style.display = "block";
  } 
  else {
    x.style.display = "none";
  }
};