(function($) {

    var params = {};
    var defaults = {
        datapath: '/media/js/iscc.json.js',
        calcpath: ''
    };
    var currents = {};
    
    var methods = {
    
        init: function(params) {
            var params = $.extend(defaults, params);
            if(!$(this).data('fastOrder')) {
                $(this).data('fastOrder', true);
                currents.master = $(this);
                return $(this).each(function() {
                
                    /* Если работаем со сборными тиражами */
                    if($(this).attr('iscc') == 'true') {
                        /* Подгружаем данные по указанному в параметрах пути */
                        $.getJSON(params.datapath, function(data){
                            currents.cc_data = data;
                            console.log(data);
                        });
                    }
                    else {
                        
                    }
                
                    /* Вешаем обработчики на все вложенные инпуты */
                    $(this).find(':input').each(function(){
                        if($(this).attr('name')) {
                            currents[$(this).attr('name')] = methods.value.apply(this);
                            $(this).change(function(){
                                $(currents.master).find('.auto').remove();
                                currents[$(this).attr('name')] = methods.value.apply(this);
                                methods.calc.apply(this);
                            });
                        }
//                        methods.calc.apply(this);
                    });

                    $('#order_summary > p > label[id]').mouseover(function(){ if($(':input[name="'+$(this).attr('id')+'"]').length) $(':input[name="'+$(this).attr('id')+'"]').closest('div').addClass('note'); });
                    $('#order_summary > p > label[id]').mouseout(function(){ if($(':input[name="'+$(this).attr('id')+'"]').length) $(':input[name="'+$(this).attr('id')+'"]').closest('div').removeClass('note'); });
                    
                    $(':submit[form="'+$(currents.master).attr('id')+'"], #'+$(currents.master).attr('id')+' :submit').click(function(){
                        $(currents.master).submit();
                    });
                    
                });
            }
            else return this;
        },
        
        redraw: function() {
        
            if(currents.cc_data && currents.cc_data.length) {
                var time = parseInt(currents.time);
            
                $(':input[name="circulation"] > option').attr('disabled', true);
                $(':input[name="paper"] > option').attr('disabled', true);
                $(':input[name="format"] > option').attr('disabled', true);
    
                for(paper in pricelist[parseInt(time)]) {
                    $(':input[name="paper"] > option[value="'+paper+'grm"]').attr('disabled', false);
                    for(format in pricelist[parseInt(time)][paper]) {
                        $(':input[name="format"] > option[value="'+format+'"]').attr('disabled', false);
                        for(color in pricelist[parseInt(time)][paper][format]) {
                            for(quant in pricelist[parseInt(time)][paper][format][color]) {
                                $(':input[name="circulation"] > option[value="'+quant+'"]').attr('disabled', false);
                            }
                            break ;
                        }
                    }
                }
            }
            
            /* Перебираем все инпуты, чтобы... */
            $(currents.master).find(':input[name]').each(function(){

                /* ...проверить доступность текущей опции */
                if($(this).children('option:selected').attr('disabled')) {
                    $(this).parent().append($('<div />').addClass('auto'));
                    currents[$(this).attr('name')] = $(this).children('option').not(":disabled").first().attr('selected', true).val();
                }
                
                /* ...перерисовать весь блок «summary» */
                var value = currents[$(this).attr('name')];
                switch($(this).attr('name')) {
                    case 'paper':       value = $(this).val().substr(0, $(this).val().length-3); break;
                    case 'chromacity':  value = (value == '4x0') ? 'односторонней' : 'двухсторонней'; break;
                    case 'time':        value += (value == '48') ? ' часов' : ' часа'; break;
                } 
                if($('label[id="'+$(this).attr('name')+'"]').length) $('label[id="'+$(this).attr('name')+'"]').html(value);
                
            });

            if($('#order_summary > p').is(':hidden')) $('#order_summary > p').fadeIn();
            
        },
        
        summary: function() {
            var value = currents[$(this).attr('name')];
            switch($(this).attr('name')) {
                case 'paper':       value = $(this).val().substr(0, $(this).val().length-3); break;
                case 'chromacity':  value = (value == '4x0') ? 'односторонней' : 'двухсторонней'; break;
                case 'time':        value += (value == '48') ? ' часов' : ' часа'; break;
            } 
            if($('label[id="'+$(this).attr('name')+'"]').length) $('label[id="'+$(this).attr('name')+'"]').html(value);
            
        },
        
        value: function(data) {
            if(!data) {
                if($(this).is(':radio')) return $(':radio[name="'+ $(this).attr('name') +'"]:checked').val();
                else return $(this).val();
            }
        },
        
        error: function(factor) {
            var message = 'ERROR: ';
            switch(factor) {
                case 'time':    message += 'Необходимо выбрать время печати'; break;
                case 'quant':   message += 'Необходимо выбрать тираж продукции'; break;
                default:        message += factor; break;
            }
//            console.log(message);
        },
        
        calc: function() {
            methods.redraw.apply(this);
            
            /* Если есть статические данные (сборные тиражи) */
            if(currents.cc_data && currents.cc_data.length) { 
                if(currents.time && currents.cc_data.pricelist[currents.time]) {
                    tmp=pricelist[currents.time];
                    if(currents.paper && tmp[currents.paper.substr(0, currents.paper.length-3)]) {
                        tmp=tmp[currents.paper.substr(0, currents.paper.length-3)];
                        if(currents.format && tmp[currents.format]) {
                            tmp=tmp[currents.format];
                            if(currents.chromacity && tmp[currents.chromacity]) {
                                tmp = tmp[currents.chromacity];
                                if(currents.circulation && tmp[currents.circulation]) {
                                    $("#price big").html(tmp[currents.circulation]);
                                    return tmp[currents.circulation];
                                }
                                else return methods.error.apply(this, Array('quant'));
                            }
                            else return methods.error.apply(this, Array('chromacity'));
                        }
                        else return methods.error.apply(this, Array('format'));
                    }
                    else return methods.error.apply(this, Array('paper'));
                }
                else return methods.error.apply(this, Array('time'));
            }
        }
        
    };
    
    $.fn.fastOrder = function(method) {
        
        if(methods[method]) return methods[method].apply(this, Array.prototype.slice.call(arguments, 1));
        else if(typeof method === 'object' || ! method) return methods.init.apply(this, arguments);
        else $.error('fastOrder error when calling: ' +  method);
        
    };
}) (jQuery);

$(document).ready(function(){
    $('#orderpanel').fastOrder({});
});