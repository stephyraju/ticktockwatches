$(document).ready(function() {
    // messages timeout for 10 sec 
    setTimeout(function() {
        $('.messages').fadeOut('slow');
    }, 10000); // <-- time in milliseconds, 1000 =  1 sec

//     // delete message
//     $('.del-msg').live('click',function(){
//         $('.del-msg').parent().attr('style', 'display:none;');
//     })
});
function myFunction() {

 var x = document.getElementById("searchDiv");
  if (x.style.display === "none") {
    x.style.display = "block";
  } else {
    x.style.display = "none";
  }
    
    /*if (document.getElementById("form").style.display === "none") {
        
        document.getElementById("form").style.display = "block";
        } 
    else {
        document.getElementById("form").style.display = "none";
    }*/
}