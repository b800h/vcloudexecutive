from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'executive.views.home', name='home'),
    url(r'^cloudcontrol/ajax/', include('cloudcontrol.urlsajax')),
    url(r'^cloudcontrol/', include('cloudcontrol.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
