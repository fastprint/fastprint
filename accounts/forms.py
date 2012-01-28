# -*- coding: utf-8 -*
from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label=u'e-mail', max_length=30, required=True)
    password = forms.CharField(label=u'Пароль', widget=forms.PasswordInput, min_length=4, required=False)


class ProfileForm(forms.Form):
    first_name = forms.CharField(label=u'Имя', max_length=30, required=True)
    last_name = forms.CharField(label=u'Фамилия', max_length=30, required=True)
    #password = forms.CharField(label=u'Пароль', widget=forms.PasswordInput(render_value=False), min_length=4, required=True)
    email = forms.EmailField(label=u'E-mail', widget=forms.TextInput(attrs={'readonly':'readonly'}), required=True)
    phone = forms.CharField(label=u'Контактный телефон', max_length=10, required=True)
    img = forms.ImageField(label=u'Ваш автар или логотип', required=False)
    is_legal = forms.CharField(widget=forms.HiddenInput())
    
    error_css_class = 'error'
    required_css_class = 'required'


class LegalForm(forms.Form):
    legal_name = forms.CharField(label=u'Название организации', max_length=100, required=True)
    inn = forms.CharField(label=u'ИНН', max_length=12, required=True)
    kpp = forms.CharField(label=u'КПП', max_length=9, required=True)
    bik = forms.CharField(label=u'БИК', max_length=9, required=True)
    rs = forms.CharField(label=u'Расчетный счет', max_length=25, required=True)
    ks = forms.CharField(label=u'Корр. счет', max_length=20, required=True)
    post = forms.CharField(label=u'Почтовый адрес', max_length=255, required=True)

    error_css_class = 'error'
    required_css_class = 'required'


class DeliveryForm(forms.Form):
    delivery_name = forms.CharField(label=u'Заголовок адреса доставки', required=False)
    city = forms.CharField(label=u'Город', initial=u'Санкт-Петербург', max_length=100, required=True)
    address = forms.CharField(label=u'Строка адреса', max_length=255, required=True)

    error_css_class = 'error'
    required_css_class = 'required'
    