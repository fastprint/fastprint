# -*- coding: utf-8 -*-
import datetime
from django.db import models
from django.contrib import admin

class Company(models.Model):
    name = models.CharField(max_length=150)

    def __unicode__(self):
        return self.name

class Chromaticity(models.Model):
    chromaticity = models.CharField(max_length=3, default='0+0')

    def __unicode__(self):
        return self.chromaticity

class PaperWeight(models.Model):
    paper_weight = models.CharField(max_length=7)

    def __unicode__(self):
        return self.paper_weight

class Format(models.Model):
    description = models.CharField(max_length=50, blank=True)
    width = models.IntegerField(max_length=4, blank=True, default=0)
    height = models.IntegerField(max_length=4, blank=True, default=0)

    def __unicode__(self):
        return self.description + ' ' + str(self.width) + 'x' + str(self.height)

class Circulation(models.Model):
    circulation = models.IntegerField(max_length=7)

    def __unicode__(self):
        return str(self.circulation)

class PrintTime(models.Model):
    print_time = models.IntegerField(max_length=3)

    def __unicode__(self):
        return str(self.print_time)

class Product(models.Model):
    cost = models.FloatField()
    company = models.ForeignKey(Company, blank=True)
    chromaticity = models.ForeignKey(Chromaticity, blank=True)
    paper_weight = models.ForeignKey(PaperWeight, blank=True)
    format = models.ForeignKey(Format, blank=True)
    circulation = models.ForeignKey(Circulation, blank=True)
    print_time = models.ForeignKey(PrintTime, blank=True)
    grub_time = models.DateTimeField(default=datetime.datetime.now())

class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name',)

class ChromaticityAdmin(admin.ModelAdmin):
    list_display = ('chromaticity',)

class PaperWeightAdmin(admin.ModelAdmin):
    list_display = ('paper_weight',)

class FormatAdmin(admin.ModelAdmin):
    list_display = ('description', 'width', 'height',)

class CirculationAdmin(admin.ModelAdmin):
    list_display = ('circulation',)

class PrintTimeAdmin(admin.ModelAdmin):
    list_display = ('print_time',)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('format', 'print_time', 'cost',)

admin.site.register(Company, CompanyAdmin)
admin.site.register(Chromaticity, ChromaticityAdmin)
admin.site.register(PaperWeight, PaperWeightAdmin)
admin.site.register(Format, FormatAdmin)
admin.site.register(Circulation, CirculationAdmin)
admin.site.register(PrintTime, PrintTimeAdmin)
admin.site.register(Product, ProductAdmin)
