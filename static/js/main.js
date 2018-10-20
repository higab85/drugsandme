
var $animationSpeed = 500;



// will ckeck whether there is more to read on harm-reduction-stage-descriptions
// and if not, will hide 'read more' button
(function( $ ){
   $.fn.parentSizeChecker = function() {

     if($(this).find('div').first().height() < 300)
       $(this).find('div:nth-child(2)').addClass('d-none');
     else
       $(this).find('div:nth-child(2)').removeClass('d-none');

   };
})( jQuery );


// add sticky-navbar after cover

// // When the user scrolls the page, execute myFunction
// window.onscroll = function() {myFunction()};

// Get the header
var header = document.getElementById("navbar");
var article = document.getElementById("article");

// // Get the offset position of the navbar
// var sticky = article.offsetTop;
//
// // Add the sticky class to the header when you reach its scroll position. Remove "sticky" when you leave the scroll position
// function myFunction() {
//   if (window.pageYOffset >= sticky) {
//     header.classList.add("sticky-navbar");
//   } else {
//     header.classList.remove("sticky-navbar");
//   }
// }

$(document).ready(function(){

  // open external links in new tab
  $('a').click(function(e){
        e.preventDefault();
        var url = $(this).attr('href');
        console.log(url);
        var pat = /^https?:\/\//i;
        if (pat.test(url))
            window.open(url, '_blank');
        else
            window.open(url, '_self')
  });

  var slug;
  slug= window.location.pathname.split('/');
  slug = slug[slug.length - 2];
  if (slug == 'en')
  slug = "index"
  $('.site-wrapper').attr('id',slug)


  var docWidth = document.documentElement.offsetWidth;

  [].forEach.call(
    document.querySelectorAll('*'),
    function(el) {
      if (el.offsetWidth > docWidth) {
        console.log(el);
      }
    }
  );


  $(".navbar-brand-item").hover(function(){
    $(this).find(".navbar-brand-dropdown").removeClass("d-none");
    $(this).find("i").toggleClass("d-none");
  }, function(){
    $(this).find(".navbar-brand-dropdown").addClass("d-none");
    $(this).find("i").toggleClass("d-none");
  });


  var $currentDrug = $('.cover__text>h1').html();


  $(".sidebar__contents__item a").click(function(event){
          event.preventDefault();
          $('html,body').animate({scrollTop:$(this.hash).offset().top}, 500);
      });
//------ cover drugs+me collapsable content ----------------------------------
  $(".title__item").stop().hover(function() {
        var $displacedMarginLeft = "9px";
        var $displacedMarginTop = "9px";
        if($(window).width() < 768){
            $displacedMarginLeft = "1.5vw";
            $displacedMarginTop = "1.5vw";
          }

        $(this).children(".title__collapse").stop().removeClass("d-none");
        $(this).children('.title__button').stop().animate({
          marginTop: $displacedMarginTop,
          marginLeft: $displacedMarginLeft
        }, $animationSpeed);
        $(this).children(".title__collapse").animate({
          opacity: 1
        }, $animationSpeed);
        return false;
    },function(){
        $(this).children('.title__button').stop().animate({
          marginTop:'0px',
          marginLeft:'0px'
        }, $animationSpeed);
        $(this).children(".title__collapse").stop().animate({
          opacity: 0
        }, $animationSpeed, function(){
          $(this).addClass("d-none");
          return false;
        });
        return false;
  });

// ---------- Search -------------------------------------------
  $('.search__input').on('input', function(){
      //unentitle item if any is entitled
      if($('.search__results__item__link').hasClass('entitled')){
          $('.entitled').unEntitle();
      }

      var thisSearchBox = this;
      $(window).keyup(function(event){
          "use strict";
          var searchquery = thisSearchBox.value.toLowerCase();

          //hide and show items
          $(".search__results__item ul:Contains('" + searchquery + "')").parentsUntil(this, '.search__results__item').removeClass('d-none');
          $(".search__results__item ul:not(:Contains('" + searchquery + "'))").parentsUntil(this, '.search__results__item').addClass('d-none');
          if(searchquery == ""){
            $(".search__results").addClass('d-none');
          }
          else {
            $(".search__results").removeClass('d-none');
            if(event.keyCode == 13){
                window.location.href = $(".tag:Contains('" + searchquery + "')").parentsUntil(this, '.search__results__item').find(">:first-child").attr("href");
              }

          }

         //changes h5 to tag names
          $(".tag:Contains('" + searchquery + "')").each(function(){
              var current = $(this).text();
              $(this).parentsUntil(this, '.search__results__item').find("a").html(current);
              $(this).parentsUntil(this, '.search__results__item').find("a").removeClass('d-none');
            //capitalise first letter of element
            $('.search__results__item__link').css('textTransform', 'capitalize');
          });

      });
  });

  // adds class to hovered content item, and only removes the class
  // if that element isn't active
  $('.sidebar__list__item__link').hover(function(){
    $(this).addClass('sidebar__list__item__link--hovered');
  },function(){
      $(this).removeClass('sidebar__list__item__link--hovered');
  });


  // Flips .thing-to-take
  $('.things-to-take__element').click(function(){
    $(this).toggleClass('things-to-take__element--flipped');
    $(this).children().toggleClass('d-none');
  });

  // Toggles stages on harm-reduction table
  $('.harm-reduction-stage-indicator').click(function(){
    var $currentStage = $(this);
    $(this).parent().children().removeClass('active');
    $(this).parent().children().removeClass('theme-bg');
    $(this).addClass('active');
    $(this).addClass('theme-bg');
    $('#harm-reduction-stage-descriptions').removeClass('full-length');
    $('#harm-reduction-stage-descriptions:nth-child(2)').find('p').text('Read more');
    $('#harm-reduction-stage-descriptions div').first().replaceWith("<div class='harm-reduction-stage-description'>" + $currentStage.find("div").html() + "</div>");
    // will ckeck whether there is more to read on harm-reduction-stage-descriptions
    // and if not, will hide 'read more' button
    $('#harm-reduction-stage-descriptions').parentSizeChecker();

    // if($('#harm-reduction-stage-descriptions div').first().height() < 300)
    //   $('#harm-reduction-stage-descriptions div:nth-child(2)').addClass('d-none');
    // else
    //   $('#harm-reduction-stage-descriptions div:nth-child(2)').removeClass('d-none');
  });
  // gives harm-reduction "BEFORE" tab it's description
  $('#harm-reduction-stage-descriptions div').first().replaceWith("<div class='harm-reduction-stage-description'>" + $('.harm-reduction-stage-indicator').first().find("div").html() + "</div>");
  // $('#harm-reduction-stage-descriptions').parentSizeChecker();

  // makes read-more buttons expand table so rest of
  // text is readable
  $('.read-more').click(function(){
    $(this).parent().toggleClass('full-length');
    if ($(this).parent().hasClass('full-length')) {
      $(this).find('p').text('Read less');
    }
    else{
      $(this).find('p').text('Read more');
    }
    $('#harm-reduction-stage-descriptions').parentSizeChecker();
  });

  // Makes first drug in #interactions-combo-addition the current drug
  // NOTE: Necessary?
  // $('.theme-color').addClass( $currentDrug.toLowerCase());
  // $('.theme-bg').addClass( $currentDrug.toLowerCase());


  // Gives each drug interaction their background colour depending on their
  // risk
  $('#interactions-table>a').each(function(){
    var $category = $(this).find('.interaction-table__elem__interaction').find('p').attr('class');
    $(this).addClass($category);
  });


  // Selects drug in combo chart:
  // - makes selected drug background-color change to color
  // - adds new info to #interactions-combo
  $('#interactions-table').on("click", '.interactions-table__elem', function(){
    $('.interactions-table__elem').addClass('combo-not-active');
    $('.interactions-table__elem.active').removeClass('active');
    $(this).removeClass('combo-not-active');
    $(this).addClass('active');
    $('#interactions-combo-addition-temp').text($(this).find('.interaction-table__elem__interaction__name').html());
    $('.interactions__combo__result__title').html($(this).find('.interaction-table__elem__interaction').find('h4').text());
    $('.interactions__combo__result__description').html($(this).find('.interaction-table__elem__interaction').find('p').text());
  });
  // Deactivates an activated drug if it is clicked on.
  $('#interactions-table').on("click", '.active', function(){
    $(this).addClass('combo-not-active');
    $(this).removeClass('active');
    $('#interactions-combo-addition-temp').text("?");
    $('.interactions__combo__result__title').text("SELECT A DRUG");
    $('.interactions__combo__result__description').text("Click one of the drugs below and see how it mixes with " + $currentDrug + ".");
  });

  // Lets you peek into the colour of the drug by only hovering over it
  $(".combo-not-active").hover(function(){
    $(this).removeClass('combo-not-active');
  },function(){
    if(!$(this).hasClass('active'))
      $(this).addClass('combo-not-active');
  })

  // makes harm reduction box on index expandable on click (mobile)
  $('#index-harm-reduction').click(function(){
      if($(this).hasClass('active')){
        $(this).find('#index-harm-reduction-content').addClass('d-none-xs d-none-sm');
        $(this).removeClass('active');
      }else{
        $('#index-blurb .active').find('#index-harm-reduction-content').removeClass('d-none-xs d-none-sm');
        $('#index-blurb .active').removeClass('active');
        $(this).addClass('active');
        $(this).find('#index-harm-reduction-content').removeClass('d-none-xs d-none-sm');
      }
    })

    // brain-science content expander
    $('.brain-science>img').click(function(){
      $(this).parent().find('.brain-science-content').toggleClass('d-none');
      $(this).parent().find('.click-me-tip').toggleClass('d-none');
    })
    // end navbar buttons

    // clickable elements' tooltips
    // $('.tooltips').tooltip();
//------------------ front page bottom buttons ------------------------------

  // $('.home-button').click(function(){
  //   $('p', this).toggleClass('d-none');
  //   $(this).siblings().find('p').addClass('d-none');
  // })

//   $('#home-buttons a').click(function (e) {
//   e.preventDefault()
//   $(this).tab('show')
// })
});
