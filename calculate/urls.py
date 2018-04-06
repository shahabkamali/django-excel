#from django.conf.urls.defaults import *
from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.index),
    url(r'admin$', views.admin),
    url(r'admin/ret_json/$', views.ret_json),
    # url(r'ajax_req$', views.ajax_req),
]