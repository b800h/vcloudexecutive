from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'cloudcontrol.views.main', name='main'),
    url(r'^$', 'cloudcontrol.views.login', name='login')
)