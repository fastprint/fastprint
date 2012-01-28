#!/usr/bin/env python
# -*- coding: utf-8 -*
from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User

class Profile(models.Model):

    ''' Базовый профиль (ФЛ) '''

    user = models.OneToOneField(User)
    img = models.ImageField(upload_to='user_pic/', blank=True, verbose_name='аватар')
    phone = models.IntegerField(max_length=18, verbose_name=u'контактный телефон')
    is_legal = models.BooleanField(default=False, blank=True, verbose_name=u'является ЮЛ')
    rating = models.IntegerField(default=0, blank=True, verbose_name=u'рейтинг заказчика')
    comment = models.TextField(verbose_name=u'комментарий к заказчику', blank=True)

    def __unicode__(self):
        return self.user.first_name + ' ' + self.user.last_name

class Legal(models.Model):

    ''' Юридическое лицо '''
    profile = models.ForeignKey(Profile)
    title = models.CharField(max_length=100, verbose_name=u'название организации')
    inn = models.PositiveIntegerField(max_length=12, verbose_name=u'ИНН', unique=True)
    kpp = models.PositiveIntegerField(max_length=10, verbose_name=u'КПП', unique=True)
    bik = models.PositiveIntegerField(max_length=10, verbose_name=u'БИК')
    rs = models.PositiveIntegerField(max_length=35, verbose_name=u'расчетный счет')
    ks = models.PositiveIntegerField(max_length=35, verbose_name=u'корр. счет')
    post = models.CharField(max_length=255, verbose_name=u'почтовый адрес')

    class Meta():
        unique_together = ('title', 'inn')

    def __unicode__(self):
        return self.title


class Delivery(models.Model):
    profile = models.ForeignKey(Profile)
    title = models.CharField(max_length=100, verbose_name=u'заголовок')
    city = models.CharField(max_length=100, verbose_name=u'город')
    address = models.CharField(max_length=255, verbose_name=u'адрес доставки')

    def __unicode__(self):
        return self.address

admin.site.register(Profile)
admin.site.register(Legal)
admin.site.register(Delivery)