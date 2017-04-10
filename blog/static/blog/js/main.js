console.log("Hello World");

$("#rightBar").css("top", "300px")
window.addEventListener('scroll', function(e){   
    element = document.getElementById("rightBar");
    pushpin();
});

var pushpin = function() {
    
    console.log($("#rightBar").offset().top);
    //console.log(element.style)
    if(screen.width > 768 && $("#rightBar").offset().top > 550) {
       element.setAttribute("style", "position: fixed;");
       element.style.top =  500 - window.scrollY * 0.5+ 'px';
    }
    else {
        element.setAttribute("style", "position: static");
    }
    
}