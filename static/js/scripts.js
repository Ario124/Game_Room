window.addEventListener('DOMContentLoaded', event => {
    // Toggle the side navigation
    const sidebarToggle = document.body.querySelector('#sidebarToggle');
    const sidebarTogglez = document.body.querySelector('#box');
    let element = document.getElementById('sidebarToggle');
    let box = document.getElementById('box');
    if (sidebarToggle) {
        sidebarToggle.addEventListener('click', event => {
            event.preventDefault();
            document.body.classList.toggle('sb-sidenav-toggled');
            localStorage.setItem('sb|sidebar-toggle', document.body.classList.contains('sb-sidenav-toggled'));
        });
    }



});


// Touch/Swipe the side navigation
// A least 100 px are a swipe
// You can use the value relative to screen size: gestureZone.innerWidth * .1
let xDown, yDown
const offset = 100;


const gestureZone = document.getElementById('side-nav-button');

gestureZone.addEventListener('touchstart', e => {
    const firstTouch = getTouch(e);
  
    xDown = firstTouch.clientX;
    yDown = firstTouch.clientY;
  });

  gestureZone.addEventListener('touchend', e => {
    if (!xDown || !yDown) {
      return;
    }
  
    const {
      clientX: xUp,
      clientY: yUp
    } = getTouch(e);
    const xDiff = xDown - xUp;
    const yDiff = yDown - yUp;
    const xDiffAbs = Math.abs(xDown - xUp);
    const yDiffAbs = Math.abs(yDown - yUp);
  
    // at least <offset> are a swipe
    if (Math.max(xDiffAbs, yDiffAbs) < offset ) {
      return;
    }
  
    if (xDiffAbs > yDiffAbs) {
      if ( xDiff > 0 ) {
        document.body.classList.remove('sb-sidenav-toggled');
      } else {
        document.body.classList.add('sb-sidenav-toggled');
      }
    } else {
      if ( yDiff > 0 ) {
        console.log('up');
      } else {
        console.log('down');
      }
    }
  });
  
  function getTouch (e) {
    return e.changedTouches[0]
  }