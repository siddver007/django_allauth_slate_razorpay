
jQuery(document).ready(function() {
	
    /*
        Fullscreen background
    */
    $.backstretch("/static/form/assets/img/backgrounds/1.jpg");
    
    $('#top-navbar-1').on('shown.bs.collapse', function(){
    	$.backstretch("resize");
    });
    $('#top-navbar-1').on('hidden.bs.collapse', function(){
    	$.backstretch("resize");
    });
    
    
    $('.registration-form input, .registration-form textarea').on('focus', function() {
        $(this).removeClass('input-error');
    });
    
    $('.registration-form').on('submit', function(e) {
        
        
        $(this).find('input, textarea').each(function(){
            if( $(this).val() == "" ) {
                e.preventDefault();
                $(this).addClass('input-error');
            }
            else {

                $(this).removeClass('input-error');
            }
        });
        
    });

        
    
});
