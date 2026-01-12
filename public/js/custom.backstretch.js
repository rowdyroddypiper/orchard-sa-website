(function($) {

	// preparing images
    var n = $('div.slides ul > li').length;
    var l = $('div.slides ul li');
    var b = $('body');
    var src = [];
    var cap = [];
    for (var i = 0; i < n; i++) {
        src[i] = $(l).eq(i).find('img').attr('src');
        cap[i] = $(l).eq(i).find('span');
    };

    // initializing backstretch.js for background
    $(b).backstretch(src, {duration: 7000, fade: 750, lazyload: true});

    $(b).on('backstretch.before', function() {
        $(this).data("backstretch").index;
        //alert('before bacstretch');
        $('.caption').fadeOut(750);
    });
        
    // coordinating image captions with slides
    $(b).on('backstretch.show', function() {
        $(this).data("backstretch").index;
        $(".caption").html(cap[$(this).data("backstretch").index].html()).fadeIn(750);
    });
	
	$(".next").click(function() {
		$(b).data('backstretch').next();
	});
	$(".prev").click(function() {
		$(b).data('backstretch').prev();
	});

})(jQuery);
