#!/usr/bin/env python
# -*- coding:utf-8 -*-
from django.conf.urls import url,include
from django.views.static import serve
from myblog import settings
from . import views

urlpatterns = [
    url(r'^hello/$',views.hello),
    url(r'^$', views.index,name='index'),
    url(r'^ueditor/', include('DjangoUeditor.urls')),
    url(r'^list-(?P<lid>\d+).html',views.list,name='list'),
    url(r'^show-(?P<sid>\d+).html',views.show,name='show'),
    url(r'^tag/(?P<tag>\w+)/$',views.tag,name='tag'),
    url(r'^s/',views.search,name='search'),
    url(r'^about',views.about,name='about'),
    url(r'^media/(?P<path>.*)$',serve ,{'document_root':settings.MEDIA_ROOT})
]