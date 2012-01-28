# -*- coding: utf-8 -*
from django.db import models
from django.contrib import admin
from store.send_html_mail import send_html_mail
from django.contrib.auth.models import User

class ccOrder(models.Model):
    client = models.IntegerField(verbose_name = 'идентификатор клиента')
    product = models.CharField(max_length = 100, verbose_name = 'продукт')
    format = models.CharField(max_length = 100, verbose_name = 'формат',)
    time = models.IntegerField(verbose_name = 'время выполнения')
    circulation = models.IntegerField(verbose_name = 'тираж')
    paper = models.CharField(max_length = 100, verbose_name = 'бумага',) # This will be foreign key for paper class
    chromacity = models.CharField(max_length = 100, verbose_name = 'цветность',)
    file1 = models.FileField(upload_to='client_files/', blank=True, verbose_name = 'лицевая сторона')
    file2 = models.FileField(upload_to='client_files/', blank =True, verbose_name = 'оборотная сторона')
    file_1c = models.FileField(upload_to='client_files/', blank=True, verbose_name='файл 1С импорта')
    cost = models.DecimalField(max_digits = 10, decimal_places = 2, verbose_name = 'стоимость')
    not_cash = models.BooleanField(default = False, verbose_name = 'Не наличные')
    need_deliver = models.BooleanField(default = False, verbose_name = 'требуется доставка')
    is_delivered = models.BooleanField(default = False, verbose_name = 'доставлено')
    order_status = models.IntegerField(verbose_name = 'статус заказа')
    enter_date = models.DateTimeField(blank =True,verbose_name = 'дата поступления заказа')
    end_date = models.DateTimeField(blank = True, verbose_name = 'ориентировочная дата выполнения заказа')

    def save(self):
        user = User.objects.get(id = self.client)
        send_html_mail(u'Ваш заказ изменён', user.email, {'order_info': self}, 'emails/order_status_changed_mail.html', sender='admin@fastprint.me')
        super(ccOrder, self).save()
    
    def __unicode__(self):
        return self.product + ' ' + unicode(self.time) + ' ' + unicode(self.format)

admin.site.register(ccOrder)