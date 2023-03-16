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

function truncate(height) {
  let descs = document.getElementsByClassName("desc");
  function getHeight(elt) { return elt.getBoundingClientRect().height; }
  function shorten(str)   { return str.slice(0, -1); }
    
  for (let i = 0; i<descs.length; i++)
  {
    elt = descs[i];
    content = elt.textContent;
    while (getHeight(elt) > height && content) {
      elt.textContent = (content = shorten(content)) + '...';
    }
  } 
}
