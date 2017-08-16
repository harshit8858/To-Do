from django.conf.urls import include, url
from django.contrib import admin
from tapp.views import *


urlpatterns = [

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', home, name='home'),
    url(r'^entry/$', entry, name='entry'),
    url(r'^delete/(\d+)$', delete, name='delete'),
    url(r'^search/$', search),
    url(r'^edit/(\d+)/$', edit, name="edit"),
    url(r'^detail/(\d+)/$', detail, name="detail"),


]
