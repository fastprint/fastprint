$(document).ready(function(){

	/* Поключение табов */
	$('.tabed').tabs({
		selected: $('.tabed a[href="#'+window.location.hash.substr(5)+'"]').parent().index(),
		fx: { opacity: 'toggle', duration: 'fast' },
		select: function(event, ui) { window.location.hash = '#tab-'+ui.tab.hash.substr(1); },
	});
	
	/* Подключение под-табов */
	$('.tabed > div').tabs({
		selected: 0,
		fx: { opacity: 'toggle', duration: 'fast' }
	});
	
	/* Связываем описание опций с панелью онлайн-заказа */
	$('.proptions > div > ul > li > a').click(function(){
		var optname = $(this).attr('itemref').substr(4);
		var optvalue = $(this).attr('href').substr(5);
		var orderopt = $('#orderpanel :input[name="'+optname+'"]');
		if($(orderopt).length) {
			$(orderopt).children('option').attr('selected', false);
			$(orderopt).children('option[value="'+optvalue+'"]').attr('selected', true);
		}
	});
	
	/* Контролируем «свои» формы */
    $('form.forma').forma();
});