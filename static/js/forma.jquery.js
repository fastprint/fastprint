(function($) {

	var params = {
	    'css_valid': 'valid',
	    'css_invalid': 'invalid',
	    'css_inactive': 'inactive'
	};
	var defaults = {};
	var currents = {};

	var methods = {
	
		init: function(params) {
			var params = $.extend(defaults, params);
			var init = $(this).data('forma');
			if(!init) {
				init = $(this).data('forma', true);
				return $(this).each(function() {

				    currents.form = $(this).submit(function(){ 
				        if($(this).attr('action') == '' && !$(this).attr('action').indexOf('#')) $(this).attr('action', window.location.hash);
				        return methods.validate.apply(this); 
				    });
				    
				    currents.submit = ($(this).find(':submit').length) ? $(this).find(':submit') : $(':submit[form="'+$(this).attr('id')+'"]');
				    
				    /* Отмечаем обязательные поля 
				    $(this).find(".required label").prepend($("<sup>*</sup>"))
				    */
				    
                	/* Включение/выключение дочерних опций */
                	$(':input.switcher').change(function(){
                	    if($(this).attr('checked')) {
                	        $('*[parent="'+$(this).attr('id')+'"]').show();
                		    $(':input[name="'+$(this).attr('name')+'"]').not($(this)).each(function(){
                		        $('*[parent="'+$(this).attr('id')+'"]').hide();
                		    });
                	    }
                	    else $('*[parent="'+$(this).attr('id')+'"]').hide();
                	});
                	
                	/* Фокусирвание required-контейнеров */
                	$(this).find('.required :input').focus(function(){ });
                	$(this).find('.required :input').blur(function(){ 
                	    methods.validate.apply(this, Array(this)); 
                	});

				});
			}
			else return this;
		},
		
		echo: function(message) {
			alert('jquery.forma: ' + message);
		},
		
		validate: function(input) {
		    if(input) {
		        var icon = ($(input).siblings('span.icon').length) ? $(input).siblings('span.icon') : $('<span/>').addClass('icon').appendTo($(input).parent());
    	        if(($(input).val() && $(input).val().length) || $(input).is(':checked')) {
    	            console.log($(input).attr('name')+'='+$(input).val());
    	            $(icon).removeClass('invalid').addClass('valid');
    	        }
    	        else {
    	            $(icon).removeClass('valid').addClass('invalid');
		            if($(input).closest('.required').length || $(input).is(':input[required]')) return $(currents.form).data('valid', false);
    	        }
		    }
		    else {
				$(currents.form).data('valid', true);
		        $(currents.form).find('.required:visible :input, :input:visible[required]').each(function(){ methods.validate.apply(this, Array(this)); })

                /* Отключаем сабмит невалидной формы		        
		        if($(currents.form).data('valid') == false) $(currents.submit).attr('disabled', true);
		        else $(currents.submit).attr('disabled', false);
		        */
		        
		        console.log($(currents.form).data('valid'));
		        return $(currents.form).data('valid');
		    }
		    
		},
		
	};

	$.fn.forma = function(method) {
		
		if(methods[method]) return methods[method].apply(this, Array.prototype.slice.call(arguments, 1));
		else if(typeof method === 'object' || ! method) return methods.init.apply(this, arguments);
		else $.error('jquery.forma error when calling: ' +  method);
		
	};
	
}) (jQuery);