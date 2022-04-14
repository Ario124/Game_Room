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


// Touch the side navigation
let touchstartY = 0;
let touchendY = 0;
let touchstartX = 0
let touchendX = 0

const gestureZone = document.getElementById('box');

gestureZone.addEventListener('touchstart', function(event) {
    touchstartX = event.changedTouches[0].screenX;
    touchstartY = event.changedTouches[0].screenY;
}, false);

gestureZone.addEventListener('touchend', function(event) {
    touchendX = event.changedTouches[0].screenX;
    touchendY = event.changedTouches[0].screenY;
    handleGesture();
}, false); 

function handleGesture() {
    
    // Swipe left

    if (touchendX <= touchstartX) {
        document.body.classList.remove('sb-sidenav-toggled');
    }
    
    // Swipe right
    
    if (touchendX >= touchstartX) {
        document.body.classList.add('sb-sidenav-toggled');
    }
    

    
    // Swipe directions

    if (touchendY <= touchstartY) {
        // console.log('Swiped up');
    }
    
    if (touchendY >= touchstartY) {
        // console.log('Swiped down');
    }
    
    if (touchendY === touchstartY) {
        // console.log('Tap');
    }
}