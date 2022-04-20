var lastScrollTop = 0;
$(window).scroll(function(){
  var st = $(this).scrollTop();
  var banner = $('.navbar-expand');
  setTimeout(function(){
    if (st > lastScrollTop){
      banner.fadeOut("slow");
      console.log("down");
    } else {
      banner.fadeIn("slow");
      console.log("up");
    }
    lastScrollTop = st;
  }, 140);
});