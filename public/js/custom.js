(function($) {

/* Menu Toggle - Mobile Side Navigation
----------------------------------------------- */
$('.menu-toggle').click(function() {
	$('#wrapper').toggleClass('push-left');
});

/* Disable # in main nav links
----------------------------------------------- */
$('.main-navigation a[href*="#"]').click(function(e) {
    e.preventDefault();
});

})(jQuery);
