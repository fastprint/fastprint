# -*- coding: utf-8 -*
from django import forms

class ccOrderForm(forms.Form):
    product = forms.CharField(max_length=255)
    format = forms.CharField(max_length=255)
    time = forms.IntegerField(max_value=100)
    circulation = forms.IntegerField(max_value=1000000)
    paper = forms.CharField(max_length=255)
    chromacity = forms.CharField(max_length=255)
    file1  = forms.FileField(required=False)
    file2  = forms.FileField(required=False)
    cost = forms.DecimalField(max_digits = 10, decimal_places = 2)
    not_cash = forms.BooleanField(required=False)
    need_deliver = forms.BooleanField(required=False)