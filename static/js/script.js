// messages timeout
$(document).ready(function() {
    // messages timeout for 3 sec 
    setTimeout(function() {
        $('.messages').fadeOut('slow');
    }, 3000);
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
}