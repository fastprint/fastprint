# -*- coding: utf-8 -*
import os
import uuid
import datetime
from settings import MEDIA_ROOT
from annoying.decorators import render_to
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.forms.util import ErrorList
from django.template import Library
from store.models import Product, Option, Event, Page
from store.send_html_mail import send_html_mail
from accounts.models import Profile

_rel = lambda x: os.path.join(DIRNAME, x)
register = Library()

@register.filter
def get_range(max, step):
    return range(0, max, step)

def get_product_list():
    return Product.objects.all()

def get_global_data(request):

    glob_dict = {}
    glob_dict['event'] = Event.objects.filter(start_date__lte=datetime.date.today(), end_date__gte=datetime.date.today())[0]
    glob_dict['menu'] = Page.objects.filter(visible=True).order_by('-priority', 'title')
    glob_dict['products'] = Product.objects.order_by('-priority', 'title')

    for product in glob_dict['products']:
        if product.title[0] == u'+':
            product.title = product.title[1:]
        elif product.title[-1] == u'+':
            product.title = product.title[0:-1]
    
    glob_dict['GET'] = { 'tab': 0 }
    for key in request.GET:
        glob_dict[key] = request.GET[key]
    
    if request.user.id:
        try:
            glob_dict['profile'] = Profile.objects.get(user=request.user.id)
        except Profile.DoesNotExist:
            glob_dict['profile'] = request.user.id
    
    return glob_dict

@render_to('product.html')
def product_page(request, url):
    data = get_global_data(request)
    data['current_product'] = Product.objects.get(name=url)
    data['product_parts'] = data['current_product'].parts.all().order_by('-priority')
    data['current_options'] = data['current_product'].options.all().order_by('-priority')
    return data

@render_to('product.html')
def subproduct_page(request, url1, url2):
    data = get_global_data(request)
    data['current_product'] = Product.objects.get(name=url2)
    data['current_options'] = data['current_product'].options.all()
    return data

@render_to('product_list.html')
def product_list_page(request):
    return get_global_data(request)

@render_to('info_export.html')
def plain_text(request, prod_url):
    product = Product.objects.get(name = prod_url)
    return {'product': product }

def handle_uploaded_file(f, path):
    ext = f.name.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    filename = os.path.join(path, filename)
    destination = open(os.path.join(MEDIA_ROOT, filename), 'wb+')
    for chunk in f.chunks():
        destination.write(chunk)
    destination.close()
    return filename

@render_to('index.html')
def index_page(request):
    data = get_global_data(request)
    data['page'] = Page.objects.get(name='main')
    return data
    
@render_to('flatpage.html')
def content_page(request, url1):
    data = get_global_data(request)
    data['page'] = Page.objects.get(name = url1)
    return data

@render_to('flatpage.html')
def subcontent_page(request, url1, url2):
    data = get_global_data(request)
    try:
        data['page'] = Page.objects.get(name = url1)
        data['subpage'] = Page.objects.get(name = url2, parent = data['page'])
    except:
        pass
    return data
