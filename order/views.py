# -*- coding: utf-8 -*
from annoying.decorators import render_to
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from store.views import handle_uploaded_file, get_global_data
from order.forms import ccOrderForm as Order
from settings import DIRNAME_TO_WRITABLE_DIR
from order.models import ccOrder as OrderModel
from store.send_html_mail import send_html_mail
import datetime

@login_required
@render_to('order.html')
def order(request):
    
    data = get_global_data(request)
    user_id = request.user.id

    if request.method == 'POST': # If the form has been submitted...
        order = Order(request.POST, request.FILES) # A form bound to the POST data
        if order.is_valid(): # All validation rules pass
            
            # Создаём переменные для принятых данных
            product = order.cleaned_data['product']
            format = order.cleaned_data['format']
            time = order.cleaned_data['time']
            circulation = order.cleaned_data['circulation']
            paper = order.cleaned_data['paper']
            chromacity = order.cleaned_data['chromacity']
            cost = order.cleaned_data['cost']
            not_cash = order.cleaned_data['not_cash']
            need_deliver = order.cleaned_data['need_deliver']


            # Создаём переменные для оставшихся данных,которых нет в форме
            is_delivered = False
            order_status = 0
            client = user_id

            # Создаём новый объект Заказа
            new_order = OrderModel(
                client = client,
                product = product,
                format = format,
                time = time,
                circulation = circulation,
                paper = paper,
                chromacity = chromacity,
                cost = cost,
                not_cash = not_cash,
                need_deliver = need_deliver,
                is_delivered = is_delivered,
                order_status = order_status,
                enter_date = datetime.datetime.now(),
                end_date = datetime.datetime.now(),
            )

            # Попробуем записать на сервер первый файл
            try:
                handle_uploaded_file(request.FILES['file1'], 'client_files')
                file1_is_uploadded = True
            except:
                file1_is_uploadded = False

            # Попробуем записать на сервер второй файл
            try:
                handle_uploaded_file(request.FILES['file2'], 'client_files')
                file2_is_uploadded = True
            except:
                file2_is_uploadded = False

            if file1_is_uploadded:
                new_order.file1 = request.FILES['file1']

            if file2_is_uploadded:
                new_order.file2 = request.FILES['file2']

            # Генерация txt-файла для 1C
            f = open(DIRNAME_TO_WRITABLE_DIR+'/media/orders_logs/client-'+unicode(client)+'_'+unicode(datetime.datetime.now())+'.txt', 'w')
            order_desc = unicode(client) + '|' + unicode(product) + '|' + unicode(format) + '|' + unicode(time) + '|' + unicode(circulation) + '|' + unicode(paper) + '|'  + unicode(chromacity) + '|' + unicode(cost) + '|' + unicode(not_cash) + '|' + unicode(need_deliver) + '|' + unicode(datetime.datetime.now())
            #f.write(order_desc)
            f.close()

            # Отправляем пользователю сообщение, что его заказ - принят
            send_html_mail('Ваш заказ принят', request.user.email, {'name': request.user.first_name + ' ' + request.user.last_name}, 'emails/order_sent_mail.html', sender='web@fastprint.info')

            # Сохраняем новый заказ в базу
            new_order.save()
                        

            return HttpResponseRedirect('/profile/orders/') # Redirect after POST
    else:
        order = Order() # An unbound form

    data['order'] = order
    return data

@login_required
@render_to('orders.html')
def orders_list(request):
    data = get_global_data(request)
    user_id = request.user.id
    my_orders = OrderModel.objects.filter(client = user_id)
    data['orders'] = my_orders
    return data
