# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.conf.urls.defaults import patterns, include, url
import settings
from store.views import index_page, product_page, subproduct_page, product_list_page, plain_text, content_page, subcontent_page
from order.views import order, orders_list
from accounts.views import signlogup, kickout, confirm_email
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', index_page),
    url(r'main/^$', index_page),
    url(r'^robots\.txt$', lambda r: HttpResponse("User-agent: *\nDisallow: /", mimetype="text/plain")),
    #url(r'^products/$', product_list_page),
    url(r'^plain_text/([a-z\d]+)/$', plain_text),    
    url(r'^products/([a-z\d]+)/$', product_page),
    url(r'^products/([a-z\d]+)/([a-z\d]+)/$', subproduct_page),
    url(r'^activate/([a-z\d@{1}\.]+)/([a-z\d]+)/$', confirm_email),
    url(r'^online/order/$', order),
    url(r'^profile/$', 'accounts.views.profile'),
    url(r'^profile/update/$', 'accounts.views.update'),
    url(r'^profile/orders/$', 'order.views.orders_list'),
    url(r'^accounts/login/$', signlogup),
    url(r'^login/$', signlogup),
    url(r'^logout/$', kickout),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^([a-z\d]+)/$', content_page),
    url(r'^([a-z\d]+)/([a-z\d]+)/$', subcontent_page),
    # Секция адресов, отвечающая за граббер
    url(r'^grubber/grub_data/$', 'price_grubber.views.grub_data'), # URL-паттерн для скачивания своих и прайсов конкурентов.
    url(r'^get_data/$', 'price_grubber.views.get_data'), # URL-паттерн для для возвращения всех данных из базы, обслуживает AJAX-запрос, возвращает json-объект
    url(r'^grubber/show_data/$', 'price_grubber.views.get_prices'), # URL-паттерн, который обрабатывается представлением, которое делает ajax-запрос к get_data и выводит результат на экран в виде красивых таблиц
    # url(r'^fastprintme/', include('fastprintme.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT}),
    )