(function($) {

	var plugin = jQuery.sub();

	var options = {};
	var defaults = {
		filter:		{},
		strnovalue: '---',
		tableclass: 'pricelist',
		downclass:	'down',
		upclass:	'up'
	};
	var currents = {
		response: {},
		filter: {},
		panel: {}
	}

	plugin.fn.extend({
	
		render: function(data, filter) {
			if(data && typeof(data) == 'object') methods.table.apply(this, Array(data, filter)); 
			else if(data != null) console.log('Unexpected data format: ' + typeof(data));
			else if(data == null && filter) methods.call.apply(this, Array(filter));
			else if(currents.response.data) methods.render.apply(this, Array(currents.response.data, filter));
			else console.log('No data for rendering. Call data before rendering!');
		}
		
	});

	var methods = {
	
		init: function(params) {
			options = $.extend(defaults, params);
			var init = $(this).data('fprice');
			if(!init) {
				init = $(this).data('fprice', true);
				this.addClass('plugin');
				currents.container = plugin(this);
			}

			if(typeof params == 'string' && methods[params]) return methods[params].apply(this, Array.prototype.slice.call(arguments, 1));
			else if(typeof params === 'object') { options = $.extend(defaults, params); }

			return plugin(this);
		},
		
		call: function(filter) {
			params = $.extend(options.filter, filter);
			$.ajax({
				url: '/get_data/',
				data: params,
				beforeSend: function() { $(currents.container).html('Загрузка данных...'); },
				success: function(response) {
					console.log(response);
					currents.response = response;
					$(currents.container).html('');
					methods.table.apply(this, Array(response.data, filter));
				},
				error: function() {
					currents.response = {};
					methods.apply.echo(this, 'Getting data error :(');
				}
			});
			return plugin(this);
		},

		table: function(input, filter) {
		
			var rows = 0;
			
			for(index in input) {
				
				data = input[index];
				
				for(time in data) {
	
					var table = $('<table align="center"/>').addClass(options.tableclass).attr('time', time);
	
					/* Заполняем шапку таблицы */
					var thead = $('<tr/>').appendTo($('<thead/>').appendTo(table));
					$('<th/>').html('Заголовок').appendTo(thead);
					$('<th/>').html('Цветность').appendTo(thead);
					$('<th/>').html('Стоимость').appendTo(thead);
					/* Заголовки столбцов сравнения */
					if(currents.response.deltas) {
						for(delta in currents.response.deltas) {
							$('<th/>').html("&delta;&nbsp;" + currents.response.deltas[delta]).appendTo(thead);
						}
					}
	
					for(paper in data[time]) {
						for(quant in data[time][paper]) {
							if(data[time][paper][quant] && data[time][paper][quant].length) {

								/* Получаем значение тиража и проверяем фильтруется ли он и соответствует ли фильтру */
								var circulation = data[time][paper][quant][0].circulation;
		
									/* Временно заполняем массив delta */
									for(prod in data[time][paper][quant]) {
										prod = data[time][paper][quant][prod];
										prod.delta = [prod.delta_gruppaM, prod.delta_kolorit, prod.delta_tetra];
									}
			
									/* Заполняем тело таблицы */
									var tbody = $('<tbody/>').attr('quant', circulation).attr('paper', paper).appendTo(table);
			
									/* Заголовок блока таблицы */
									$('<th/>').appendTo($('<tr/>').addClass('arow').appendTo(tbody)).attr('colspan', $(thead).children('th').length).html(circulation + ' шт. на бумаге ' + paper + ' гр/м<sup>2</sup> за ' + time + ' ч.');
			
									for(prod in data[time][paper][quant]) {
										rows++;
										prod = data[time][paper][quant][prod];
										var tr = $('<tr/>').appendTo(tbody);
										$('<td/>').html(prod.format).appendTo(tr);
										$('<td/>').html(prod.chromaticity).appendTo(tr);
										$('<td/>').html(prod.cost).appendTo(tr);
			
										/* Заполняем разницу в стоимости по всем типографиям */
										if(currents.response.deltas && prod.delta && currents.response.deltas.length == prod.delta.length) {
											for(delta in prod.delta) {
												delta = parseFloat(prod.delta[delta]);
												var td = $('<td/>').appendTo(tr);
												if(delta) {
													var arr = (delta < 0) ? "&uarr;" : "&darr;";
													var css = (delta < 0) ? options.upclass : options.downclass;
													$(td).addClass(css).html(delta + "&nbsp;" + arr);
												}
												else $(td).html(options.strnovalue);
											}
										}
									}
		//						}
							}
							else {
								console.log('Недостаточно данных для вывода по параметрам (время/бумага): ' + time + '/' + paper);
								table = null;
								continue ;
							}
						}
					}
					$(currents.container).append(table);
				}
			}
			$(currents.container).prepend(methods.panel.apply(this, Array(input)));
			$(currents.container).prepend($('<span/>').html('Успешно загружено ' + rows + 'строк'));
		},
		
		panel: function(input) {
			currents.panel = $('<fieldset/>').attr('id', 'filterpanel');//.append($('<legend/>').html('Фильтр'));
			currents.panel.time = $('<select name="time"/>').addClass('filter').append($('<option/>').html('Фильтр по времени...').attr('value', 0)).appendTo(currents.panel);
			currents.panel.paper = $('<select name="paper"/>').addClass('filter').append($('<option/>').html('Фильтр по бумаге...').attr('value', 0)).appendTo(currents.panel);
			currents.panel.quant = $('<select name="quant"/>').addClass('filter').append($('<option/>').html('Фильтр по тиражу...').attr('value', 0)).appendTo(currents.panel);
			currents.panel.submit = $('<input type="button" value="&#8596;"/>').click(function(){ methods.filter.apply(this); }).appendTo(currents.panel);

			for(index in input) {
				data = input[index];
				for(time in data) {
					if(!$(currents.panel.time).children('option[value='+time+']').length) $('<option/>').attr('value', time).html(time + ' ч.').appendTo(currents.panel.time);
					for(paper in data[time]) {
						if(!$(currents.panel.paper).children('option[value='+paper+']').length) $('<option/>').attr('value', paper).html(paper + ' г/м2').appendTo(currents.panel.paper);
						for(quant in data[time][paper]) {
							if(data[time][paper][quant][0]) {
								var q = data[time][paper][quant][0].circulation;
								if(!$(currents.panel.quant).children('option[value='+q+']').length) $('<option/>').attr('value', q).html(q + ' шт.').appendTo(currents.panel.quant);
							}
						}
					}
				}
			}
			return currents.panel;
		},
		
		filter: function(filter) {

			if(!filter) {
				filter = []
				$('select.filter').each(function(){
					if($(this).val() && $(this).val() != '0') {
						filter.push($(this).attr('name'));
					}
				});
			}

			if(filter.length) {
				var active = inactive = '';
				for(i in filter) {
					var elem = (filter[i] == 'time') ? 'table' : 'tbody';
					active += elem + '['+filter[i]+'='+$('select.filter[name="'+filter[i]+'"]').val()+'],';
					inactive += elem + '['+filter[i]+'!='+$('select.filter[name="'+filter[i]+'"]').val()+'],';
				}

				active = active.substr(0, active.length - 1);
				inactive = inactive.substr(0, inactive.length - 1);

				$(active).show();
				$(inactive).hide();
			}
		},
		
		echo: function(message) {
			alert('fprice: ' + message);
		}
				
	};

	$.fn.fprice = function(method) {
		methods.init.apply(this, Array(method));
	};
}) (jQuery);