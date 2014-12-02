from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

urlpatterns = patterns('',
    url(r'^start_server/$', 'cloudcontrol.ajax.start_server', name='ajax_start_server'),
    url(r'^stop_server/$', 'cloudcontrol.ajax.stop_server', name='ajax_stop_server'),
    url(r'^suspend_server/$', 'cloudcontrol.ajax.suspend_server', name='ajax_suspend_server'),
    url(r'^boost_server/$', 'cloudcontrol.ajax.boost_server', name='ajax_boost_server'),
    url(r'^deboost_server/$', 'cloudcontrol.ajax.deboost_server', name='ajax_deboost_server')
    )  