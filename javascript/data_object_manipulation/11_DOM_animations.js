// Here I will learn to create HTML animations using Javascript
// Javascript animations are done by programmign gradual changes
// in a element's style
// The changes are called by a timer
// When the timer interval is small, the animation looks continous

function myMove() {
    let id = null;
    const elem = document.getElementById("animate");
    let pos = 0;
    clearInterval(id);
    id = setInterval(frame, 5);
    function frame() {
        if (pos == 350) {
            clearInterval(id);
        }
        else {
            pos++;
            elem.style.top = pos + "px";
            elem.style.left = pos + "px";
        }
    }
}

myMove();