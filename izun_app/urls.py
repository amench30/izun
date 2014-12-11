from django.conf.urls import patterns, url
from izun_app import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^about$', views.about, name='about'),
        url(r'^contact$', views.contact, name='contact'),
        url(r'^blog$', views.blog, name='blog'),
        url(r'^forms$', views.forms, name='forms'),
        )
