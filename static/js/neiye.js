$(document).ready(function(){

    var swiper_solutions = new Swiper(".lksy_honorary_c", {
        slidesPerView: 4,
        spaceBetween: 30,
        autoplay:{
            delay:5000,
        },
        breakpoints: {
            1023: {
                slidesPerView: 3,
                spaceBetween: 20,
            },
            767: {
                slidesPerView: 2,
                spaceBetween: 10,
            }
        },
    });


});