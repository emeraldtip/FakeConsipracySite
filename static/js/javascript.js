var bruh = 0;
function changColor() {
    if (bruh == 0) {
      bruh = 1;
      return('#3000BE')
    }
    else if (bruh == 1) {
    	bruh = 0;
      return('#000050')
    }
}

function setColor(){
    document.getElementById("header").style.backgroundColor = changColor();
    setTimeout(setColor, 20000);
}
setColor();
