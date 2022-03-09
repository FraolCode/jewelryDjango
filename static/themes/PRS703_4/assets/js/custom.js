/*
 * Custom code goes here.
 * A template should always ship with an empty custom.js
 */



        // Parallax Background Image Js Start
		function ParallaxImage(){
			var isMobile = /Android|webOS|iPhone|iPad|iPod|BlackBerry/i.test(navigator.userAgent);
			if(!isMobile) {
				if($(".custom-parallaxblock").length){  $(".custom-parallaxblock").ParallaxBackground({  invert: false });};    
			}else{
				$(".custom-parallaxblock").ParallaxBackground({  invert: true });	
			}	
		}
		
		
		
		
		// Common Slider Image
		function initialize_owl(el) {
			el.owlCarousel({
					items: 4,
					mouseDrag: true,
					touchDrag: true,
					autoplay: false,
					responsive:{
						0:{  
								items:1  
						},
						381:{  
								items:1
						},
						480:{  
								items:2
						},
						767:{  
								items:3
						},
						991:{
								items:3	
						},
						1200:{
								items:4
						}
						
					},
					nav:true,
					loop:true,
					navText:[
						"<div class='prev-arrow'></div>",
						"<div class='next-arrow'></div>"
					]
			});
		}

		// Common Slider Image
		function initialize_fifthowl(el) {
			el.owlCarousel({
					items: 5,
					mouseDrag: true,
					touchDrag: true,
					autoplay: false,
					responsive:{
						0:{  
								items:1  
						},
						381:{  
								items:1
						},
						480:{  
								items:2
						},
						640:{  
								items:3
						},
						991:{
								items:4	
						},
						1200:{
								items:5
						}
						
					},
					nav:true,
					loop:true,
					navText:[
						"<div class='prev-arrow'></div>",
						"<div class='next-arrow'></div>"
					]
			});
		}


		function initialize_bestowl(el) {
			el.owlCarousel({
					items: 5,
					mouseDrag: true,
					touchDrag: true,
					autoplay: false,
					responsive:{
						0:{  
							items:1  
						},
						371:{  
							items:1
						},
						480:{  
							items:2
						},
						767:{  
							items:3
						},
						1200:{
							items:4	
						},
						1400:{
							items:5
						}
					},
				nav:true,
				loop:true,
				navText:[
					"<div class='prev-arrow'></div>",
					"<div class='next-arrow'></div>"
				]
			});
		}

		
		function initialize_categoryowl(el) {
			el.owlCarousel({
					items: 4,
					mouseDrag: true,
					touchDrag: true,
					autoplay: false,
					responsive:{
						0:{  
								items:1  
						},
						480:{  
								items:2  
						},
						767:{  
								items:3
						},
						992:{  
								items:3
						},
						1110:{
								items:3	
						},
						1240:{
								items:4
						}
						
					},
					nav:true,
					loop:true,
					navText:[
						"<div class='prev-arrow'></div>",
						"<div class='next-arrow'></div>"
					]
			});
		}
	
		function initialize_brandowl(el) {
			el.owlCarousel({
					items: 5,
					mouseDrag: true,
					touchDrag: true,
					autoplay: false,
					responsive:{
						0:{  
								items:2  
						},
						480:{  
								items:3
						},
						641:{  
								items:4
						},
						991:{
								items:4	
						},
						1200:{
								items:5
						}
						
					},
					nav:true,
					loop:true,
					navText:[
						"<div class='prev-arrow'></div>",
						"<div class='next-arrow'></div>"
					]
			});
		}
		
		// Single Image owl Slider
		function initialize_oneowl(elsingle) {
			elsingle.owlCarousel({
					items: 1,
					mouseDrag: true,
					touchDrag: true,
					autoplay: false,
					singleItem:true,
					nav:true,
					loop:true,
					navText:[
						"<div class='prev-arrow'></div>",
						"<div class='next-arrow'></div>"
					]
			});
	
	   }

	   function initialize_testimonialowl(elsingle) {
			elsingle.owlCarousel({
					items: 1,
					mouseDrag: true,
					touchDrag: true,
					autoplay: false,
					singleItem:true,
					nav:true,
					loop:true,
					navText:[
						"<div class='prev-arrow'></div>",
						"<div class='next-arrow'></div>"
					]
			});
	
	   }
	   

function bindGrid()
{
	var view = $.totalStorage('display');


	if (view && view != 'list')
		display(view);
	else
		$('.display').find('#grid').addClass('selected');

	$(document).on('click', '#grid', function(e){
		e.preventDefault();
		$('#products div.products').animate({ opacity: 0 }, 400);
		setTimeout(function() { display('grid'); }, 400)
		$('#products div.products').animate({ opacity: 1 }, 400);
	});

	$(document).on('click', '#list', function(e){
		e.preventDefault();
		$('#products div.products').animate({ opacity: 0 }, 400)
		setTimeout(function() {display('list');  }, 400)
		$('#products div.products').animate({ opacity: 1 }, 400);
	});
}

function display(view)
{
	if (view == 'list')
	{
		$('#products div.products').removeClass('grid').addClass('list');
		$('#products div.products > article').removeClass('col-xs-12 col-sm-6 col-md-6 col-lg-6 col-xl-4').addClass('col-xs-12');
		$('#products div.products > article').each(function(index, element) {
			var html = '';
			html = '<div class="thumbnail-container">';
				html += '<div class="row">';
					html += '<div class="thumbnail-inner col-xs-12 col-sm-5 col-md-5 col-lg-4">' + $(element).find('.thumbnail-inner').html() + '</div>';
					html += '<div class="product-description col-xs-12 col-sm-7 col-md-7 col-lg-8">';
						html += '<h1 class="h3 product-title" itemprop="name">'+ $(element).find('.product-title').html() + '</h1>';
						var price = $(element).find('.product-price-and-shipping').html();
						if (price != null) {
							html += '<div class="product-price-and-shipping">'+ price + '</div>';
						}
						html += '<p class="product-desc" itemprop="description">'+ $(element).find('.product-desc').text() + '</p>';
						var varlink = $(element).find('.variant-links').html();
						if (varlink != null) {
							html += '<div class="variant-links new-variant-list">'+ varlink +'</div>';
						}
						var colorList = $(element).find('.highlighted-informations').html();
						html += '<div class="product-add-to-cart addtocart-button">'+ $(element).find('.product-add-to-cart').html() +'</div>';
						if (colorList != null) {
							html += '<div class="highlighted-informations hidden-sm-down">'+ colorList +'</div>';
						}
					html += '</div>';
				html += '</div>';
			html += '</div>';
			$(element).html(html);
		});
		$('.display').find('li#list').addClass('selected');
		$('.display').find('li#grid').removeAttr('class');
		$.totalStorage('display', 'list');
	}
	else
	{
		$('#products div.products').removeClass('list').addClass('grid');
		$('#products div.products > article').removeClass('col-xs-12').addClass('col-xs-12 col-sm-6 col-md-6 col-lg-6 col-xl-4');
		$('#products div.products > article').each(function(index, element) {
			var html = '';
			html += '<div class="thumbnail-container">';
				html += '<div class="thumbnail-inner">' + $(element).find('.thumbnail-inner').html() + '</div>';
				
				html += '<div class="product-description">';
					html += '<h1 class="h3 product-title" itemprop="name">'+ $(element).find('.product-title').html() + '</h1>';
					var price = $(element).find('.product-price-and-shipping').html();
					if (price != null) {
						html += '<div class="product-price-and-shipping">'+ price + '</div>';
					}
				//	html += '<p class="product-desc" itemprop="description">'+ $(element).find('.product-desc').html() + '</p>';
					var colorList = $(element).find('.highlighted-informations').html();
					if (colorList != null) {
						html += '<div class="highlighted-informations hidden-sm-down">'+ colorList +'</div>';
					}
					html += '<div class="product-add-to-cart">'+ $(element).find('.product-add-to-cart').html() +'</div>';
				html += '</div>';
			
			html += '</div>';
			$(element).html(html);
		});
		$('.display').find('li#grid').addClass('selected');
		$('.display').find('li#list').removeAttr('class');
		$.totalStorage('display', 'grid');
	}
}



function leftRightColumn(){
	if ($(document).width() <= 991)
	{
		$('#wrapper .container > .row #left-column').appendTo('#wrapper .container > .row .wrapper-inner');
	}
	else if($(document).width() >= 992)
	{
		$('#wrapper .container > .row #left-column').prependTo('#wrapper .container > .row .wrapper-inner');
	}
}
	function searchwidget(){
	
	if ($(document).width() <= 991)
	{
		$('.ot-serach-outer').appendTo('.hidden-md-up.text-xs-center.mobile');
	}
	else
	{
		$('.header-top #search_widget').prependTo('.right-logo');
	}
}

function  menuarrow(){
	$('#top-menu .category').each(function() {
       	if($(this).children('.popover').length > 0) {
        	var width = $(window).width();
	   		if(width > 991){
        	$(this).addClass("arrow");
     		}else {
     		$(this).removeClass("arrow");	
     		}
     	}
     });
}

function  menuclass(){
	$('#top-menu > li').each(function() {
		
       	var x = $(this).find('.sub-menu  .top-menu li.category .collapse  .top-menu').length;
       	//alert(x);
        if(x>0){
        	$(this).addClass("flexcss");	
        }else{
        	$(this).addClass("noflex");		
        }

     

     });


}

function headertoggle() {		
		if (jQuery(window).width() >= 991)
			{
				$('#_desktop_language_selector .language-selector-wrapper .language-selector ul').removeClass('dropdown-menu');
				$('#_desktop_currency_selector .currency-selector  ul').removeClass('dropdown-menu');
				$('#_desktop_language_selector .language-selector-wrapper').appendTo('.userinfo-toggle').wrap( "<li class='language'></div>" );
				$('#_desktop_currency_selector .currency-selector').appendTo('.userinfo-toggle').wrap( "<li class='currency'></div>" );
			}
}


function staticMenuToggle(){
	jQuery(".static-categories-inner > h3 > a").click(function(){
			jQuery(this).parent().toggleClass('active').parent().find('ul').slideToggle('slow');	
	});

}


function ToggleIcon(){
			if (jQuery(window).width() <= 991)
			{
				
				jQuery(".footer_inner .footer-cms .title").click(function(){
					jQuery(this).parent().toggleClass('active').parent().find('.footer-toggle').slideToggle('slow');
				});
		
			}else{
				jQuery(".footer_inner .footer-cms .title").parent().find('ul').removeAttr('style');
				jQuery(".footer_inner .footer-cms .title").removeClass('toggle-active');
				
			}	
	}

function initializeAddtocart(){
	var carturl = $('#carturl').val();
	var carttoken = $('#carttoken').val();
	//alert(carttoken);
	$('.cart-form-url').attr('action', carturl);
	$('.cart-form-token').attr('value', carttoken);
}
function  menfix(){
$(window).scroll(function(){						
				  if ($(window).scrollTop() >= 240) {		
					$('.header-menu').addClass('fixed');		
				   }		
				   else {		
					$('.header-menu').removeClass('fixed');		
				   }		
				});
}
$(document).ready(function (){	
	// Common Slider Image Function Call
	initialize_owl($('#featuredproducts-carousel'));
	initialize_bestowl($('#bestsellers-carousel'));
	initialize_owl($('#specialproducts-carousel'));
	initialize_fifthowl($('#newproducts-carousel'));
	initialize_owl($('#accessories-carousel'));
	initialize_categoryowl($('#custom-categorybannerblock .category-banner'));
	initialize_owl($('#order-confirmation  #featuredproducts-carousel'));
	// Brand slider
	initialize_brandowl($('#brand-carousel'));
	
	// Single Image owl Slider Dunction Call
	initialize_testimonialowl($('#testimonial-slider'));
	initialize_oneowl($('#homepage-carousel'));
	
	// Parallax Image Slider Call
	ParallaxImage();
	
	// Parallax Image Slider Call
	initializeAddtocart();
	
	
	// Left And right Column After Wrapper
	leftRightColumn(); 
	headertoggle();
	searchwidget();
	staticMenuToggle();
	menuarrow();
	menuclass();
	menfix();
	// Grid lIst change
	bindGrid();

	ToggleIcon();
	
	 $('.user-icon').on("click", function(){
		$(this).parent().find('.userinfo-toggle').slideToggle();												
	 });
	 
	 $( ".search-widget input[type=text]" ).focus(function() {
		$(this).parent().parent().addClass("inputfocus");
	});
	$( ".search-widget input[type=text]" ).blur(function() {
		$(this).parent().parent().removeClass("inputfocus");
	});
	


	
	
});

$( window ).resize(function() {
	// Single Image owl Slider Dunction Call
	initialize_oneowl($('#testimonial-slider'));	
	initialize_oneowl($('#homepage-carousel'));
	
	// Left And right Column After Wrapper
	leftRightColumn(); 
	
	searchwidget();
	headertoggle();
	menuarrow();
	menuclass();


});							


$(window).load(function() {

    $(".preloading").fadeOut("slow");

});

