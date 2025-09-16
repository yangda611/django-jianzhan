$(document).ready(function(){

    $(window).on("scroll", function (e){
        var b_top = $('.lksy_banner').offset().top;
        var scroll_now = jQuery(window).scrollTop();
        if(scroll_now-b_top > 0){
            $('.lksy_top').stop().slideUp(100);
            $('header').addClass('fixed');
        }
        else{
            $('.lksy_top').stop().slideDown(100);
            $("header").removeClass("fixed");
        }
    });

    $('.lksy_menuBtn').append('<b></b><b></b><b></b>');
    $('.lksy_menuBtn').click(function(event) {
        $(this).toggleClass('open');
        $('.lksy_nav_mobile').stop().slideToggle();
        $('.lksy_nav_mobile').addClass('fixed');
    });

    var _winw = $(window).width();
        $('.lksy_ment ul li').hover(function() {
            $(this).find('.sub').stop().slideDown();
        }, function() {
            $(this).find('.sub').stop().slideUp();
        });


    $('.lksy_nav_mobile li i').click(function() {
        $(this).parents('li').toggleClass('on').siblings('li').stop().removeClass('on');
        $(this).toggleClass('on');
        if ($(this).siblings('.lksy_sub').length) {
            $(this).parents('li').siblings('li').find('.sub').stop().slideUp();
            $(this).parents('li').siblings('li').find('i').stop().removeClass('on')
            $(this).siblings('.lksy_sub').stop().slideToggle();
            return false;
        }
    });
 
   $('.lksy_nav_mobile .lksy_sub .down').click(function() {
        $(this).siblings('.lksy_sub').stop().slideToggle();
        $(this).parents('.row').siblings('.row').find('.lksy_sub').stop().slideUp();
        return false;
    });
 

    // 选项卡 鼠标点击
    $(".tab_click li").click(function(){
      var tab=$(this).parent(".tab_click");
      var con=tab.attr("id");
      var on=tab.find("li").index(this);
      $(this).addClass('on').siblings(tab.find("li")).removeClass('on');
      $(con).eq(on).addClass('on').siblings(tab.find("li")).removeClass('on');
    });
    $('.tab_click').each(function(index, el) {
        if($(this).find('li.on').length){
            $(this).find("li.on").trigger('click');
        }else{
            $(this).find("li").filter(':first').trigger('click');
        }
    });

    $(".tab_hover1 li").mouseenter(function(){
      var tab=$(this).parent(".tab_hover1");
      var con=tab.attr("id");
      var on=tab.find("li").index(this);
      $(this).addClass('on').siblings(tab.find("li")).removeClass('on');
      $(con).eq(on).addClass('on').siblings(tab.find("li")).removeClass('on');
    });
    $('.tab_hover1').each(function(index, el) {
        if($(this).find('li.on').length){
            $(this).find("li.on").trigger('mouseenter');
        }else{
            $(this).find("li").filter(':first').trigger('mouseenter');
        }
    });

   $(".tab_hover li").mouseenter(function() {
        var tab = $(this).parent(".tab_hover");
        var con = tab.attr("id");
        var on = tab.find("li").index(this);
        $(this).addClass('on').siblings(tab.find("li")).removeClass('on');
        $(con).eq(on).show().siblings(con).hide();
    });
    $('.tab_hover').each(function(index, el) {
        if ($(this).find('li.on').length) {
            $(this).find("li.on").trigger('mouseenter');
        } else {
            $(this).find("li").filter(':first').trigger('mouseenter');
        }
    });

    var swiper_news = new Swiper(".wlx_news_c", {
        slidesPerView: 3,
        spaceBetween: 30,
        autoplay:{
            delay:3000,
        },
        breakpoints: {
            1023: {
                slidesPerView: 2,
                spaceBetween: 20,
            },
            767: {
                slidesPerView: 1,
                spaceBetween: 15,
            }
        },
    });

    $(document).ready(function(){
        $('.wlx_totop').click(function(){
          $("html,body").animate({scrollTop:0});
      });
    });

});

function check(fid){
    var pattern = / \/|(pwd)|(\.html)|(script)|(select)|(from)|(print)|(\.js)|(http\:\/\/)|(https\:\/\/)|(www\.)|(\.\.\.)|(\/)|(\\)|(\$)/gim;
    var keyword = $("#"+fid+" #keyword").val().trim();
    if (keyword == '' || pattern.test(keyword)) {
        layer.msg('<span style="color:#FFF;">Please fill in the keyword and the keyword cannot consist of illegal characters!</span>');
        $("#"+fid+" #keyword").focus();
    }else{
        window.location.href="http://"+window.location.host+"?q="+keyword;
    }
}