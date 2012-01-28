# -*- coding: utf-8 -*
import os
import uuid
from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
from mptt.admin import MPTTModelAdmin
from mptt.models import MPTTModel, TreeForeignKey
from store.send_html_mail import send_html_mail

class Entity(models.Model):
    title = models.CharField(max_length = 100)
    name = models.CharField(max_length = 100)
    desc = models.TextField()
    img = models.ImageField(upload_to='storentity/', blank = True)
    priority = models.IntegerField(default=0, blank = True)

    class Meta():
        abstract = True
        ordering = ['-priority', 'title',]
        pass

    def __unicode__(self):
        return self.title    


class Option(Entity):
    cost = models.DecimalField(max_digits=10, decimal_places=2, blank=True, default=.00, verbose_name = u'стоимость опции')
    time = models.IntegerField(default=0, blank=True, verbose_name = u'время операции в секундах')
    is_cc = models.BooleanField(verbose_name = u'доступен в сборные тиражи')
    parent = models.ForeignKey('self', blank = True, null = True, verbose_name = u'принадлежит к')
    visible = models.BooleanField(default=True, verbose_name = u'показывать на странице продукта')

    class Meta:
        ordering = ('title',)

    def __unicode__(self):
        try:
            return self.parent.title + ' -> ' + self.title
        except:
            return self.title

class ProductPart(Entity):
    options = models.ManyToManyField(Option, verbose_name = u'доступные опции')

    class Meta:
        verbose_name = u'Часть продукта'
        verbose_name_plural  = u'Части продуктов'


class Product(Entity):
    is_cc = models.BooleanField(verbose_name = u'доступен в сборные тиражи') # Доступность в сборнике
    parent = models.ForeignKey('self', blank = True, null = True, verbose_name = u'принадлежит к')
    options = models.ManyToManyField(Option, verbose_name = u'доступные опции')
    parts = models.ManyToManyField(ProductPart, blank=True, verbose_name=u'состоит из частей')
    
    def __unicode__(self):
        if self.parent is not None:
            if self.title[0] == u'+':
                return self.parent.title + ' ' + self.title[1:]
            if self.title[-1] == u'+':
                return self.title[0:-1] + ' ' + self.parent.title.lower()

        return self.title


class Page(MPTTModel, Entity):
    slug = models.SlugField(blank=True)
    parent = TreeForeignKey('self', null=True, blank=True, verbose_name=u'принадлежит к')
    visible = models.BooleanField(default=True, verbose_name = u'страница видна на сайте')
    product = models.ManyToManyField(Product, blank = True, null = True, verbose_name = u'привязанные продукты')

    class MPTTMeta:
        order_insertion_by = ['desc',]
        ordering = ['-priority', 'title']


class Event(Entity):
    start_date = models.DateField(verbose_name = u'начало кампани')
    end_date = models.DateField(verbose_name = u'дата события')
    products = models.ManyToManyField(Product, verbose_name = u'набор продуктов')
    css = models.TextField(blank=True, verbose_name=u'CSS-надстройка')


class EntityAdmin(admin.ModelAdmin):
    class Media:
        js = ('js/tiny_mce/tiny_mce.js',
              'js/tiny_mce/textareas.js',)

class PageAdmin(MPTTModelAdmin):
    mptt_level_indent = 30

    class Media:
        js = ('js/tiny_mce/tiny_mce.js',
              'js/tiny_mce/textareas.js',)

class ProductAdmin(EntityAdmin):
    filter_horizontal = ('options',)

admin.site.register(Page, PageAdmin)
admin.site.register(Event, EntityAdmin)
admin.site.register(Option, EntityAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductPart, ProductAdmin)
