$(document).ready(function(){

    var swiper_banner = new Swiper(".lksy_banner", {
        preventClicks:true,
        resistanceRatio:0,
        autoplay: {
            delay: 5000,
            disableOnInteraction: false,
        },
        speed:500,
        effect: 'fade',
        pagination: {
            el: ".lksy_banner .swiper-pagination",
            clickable :true,
        },
    });


    // var swiper_choose = new Swiper(".lksy_choose_r .swiper", {
    //     preventClicks:true,
    //     direction: "vertical",
    //     autoplay:{
    //         delay:3000,
    //     },
    //     pagination: {
    //         el: ".lksy_choose .swiper-pagination",
    //         clickable :true,
    //     },
    // });


    var swiper_specialty = new Swiper(".lksy_specialty_c .swiper", {
        loop : true,
        autoplay:{
            delay:3000,
        },
        navigation: {
            nextEl: ".lksy_specialty_c .swiper-button-next",
            prevEl: ".lksy_specialty_c .swiper-button-prev",
        },
    });

    $('.lksy_text_li i').hover(
        function(){
         $(this).parent().addClass('on')
        },
        function(){
         $(this).parent().removeClass('on')
        }
    )

    var swiper_news = new Swiper(".lksy_news_zh .swiper", {
        loop:true,
        autoplay:{
            delay:3000,
        },
        pagination: {
            el: ".swiper-pagination",
            clickable :true,
        },
    });

    var swiper_newscase = new Swiper(".lksy_news_case .swiper", {
        loop:true,
        autoplay:{
            delay:3000,
        },
        pagination: {
            el: ".swiper-pagination",
            type: "fraction",
            clickable :true,
        },
    });

    // var swiper_news = new Swiper(".lksy_news_c", {
    //     slidesPerView: 3,
    //     spaceBetween: 30,
    //     autoplay:{
    //         delay:3000,
    //     },
    //     navigation: {
    //         nextEl: ".lksy_news .swiper-button-next",
    //         prevEl: ".lksy_news .swiper-button-prev",
    //     },
    //     breakpoints: {
    //         1023: {
    //             slidesPerView: 2,
    //             spaceBetween: 20,
    //         },
    //         767: {
    //             slidesPerView: 1,
    //             spaceBetween: 15,
    //         }
    //     },
    // });


    $(window).on("scroll", function (e){
        var about_top = $('.lksy_about').offset().top;
        var aboutHeight = $('.lksy_about').height();
        var scroll_now = jQuery(window).scrollTop();
        if(scroll_now < about_top){
            $('.lksy_about').addClass('on');
        }
    });


    // gsap.registerPlugin(ScrollTrigger);
    // gsap.timeline({scrollTrigger:{trigger:'.lksy_about', start:'top-=200px', end:'center center', scrub:1}})
    //     .to(".lksy_about_l img",  { y: -100 }, 0)
});

document.addEventListener('mousemove', function(event) {
    var shakediv = document.getElementById("lksy_process_img");
    var div_advc = $('.lksy_process_b').height();
    var b_top = $('.lksy_process_b').offset().top;
    if (event.pageY>=b_top && event.pageY<=b_top+div_advc) {

        var leftOffset = event.clientX;
        var rightOffset = event.clientY;
        if (leftOffset > window.innerWidth / 2 && rightOffset > window.innerHeight / 2) {
            shakediv.style.transform = 'translate(10px , 10px)';
        }
        else if(leftOffset > window.innerWidth / 2 && rightOffset < window.innerHeight / 2){
            shakediv.style.transform = 'translate(10px , -10px)';
        }
        else if(leftOffset < window.innerWidth / 2 && rightOffset > window.innerHeight / 2){
            shakediv.style.transform = 'translate(-10px , 10px)';
        }
        else{
            shakediv.style.transform = 'translate(-10px , -10px)';
        }
    }
});

