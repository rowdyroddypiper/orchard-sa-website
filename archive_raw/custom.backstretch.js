var _____WB$wombat$assign$function_____=function(name){return (self._wb_wombat && self._wb_wombat.local_init && self._wb_wombat.local_init(name))||self[name];};if(!self.__WB_pmw){self.__WB_pmw=function(obj){this.__WB_source=obj;return this;}}{
let window = _____WB$wombat$assign$function_____("window");
let self = _____WB$wombat$assign$function_____("self");
let document = _____WB$wombat$assign$function_____("document");
let location = _____WB$wombat$assign$function_____("location");
let top = _____WB$wombat$assign$function_____("top");
let parent = _____WB$wombat$assign$function_____("parent");
let frames = _____WB$wombat$assign$function_____("frames");
let opens = _____WB$wombat$assign$function_____("opens");
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
}
/*
     FILE ARCHIVED ON 06:03:03 Dec 13, 2018 AND RETRIEVED FROM THE
     INTERNET ARCHIVE ON 10:05:47 Jan 12, 2026.
     JAVASCRIPT APPENDED BY WAYBACK MACHINE, COPYRIGHT INTERNET ARCHIVE.

     ALL OTHER CONTENT MAY ALSO BE PROTECTED BY COPYRIGHT (17 U.S.C.
     SECTION 108(a)(3)).
*/
/*
playback timings (ms):
  captures_list: 0.997
  exclusion.robots: 0.094
  exclusion.robots.policy: 0.078
  esindex: 0.014
  cdx.remote: 118.08
  LoadShardBlock: 252.537 (3)
  PetaboxLoader3.datanode: 451.202 (5)
  PetaboxLoader3.resolve: 287.107 (3)
  load_resource: 593.505 (2)
*/