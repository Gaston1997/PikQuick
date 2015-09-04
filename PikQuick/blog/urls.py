# -*- coding: utf-8 -*-

from django.conf.urls import include, url , patterns

urlpatterns=patterns('',
                     url(r'^$' , 'blog.views.home' , name='home'),
                     url(r'^ver_post/(?P<id_post>[0-9]+)/$', 'blog.views.ver_post', name='vermipost'),
                     url(r'^nuevapublic$','blog.views.nuevapublic', name='nuevapublic'),
                     url(r'^crear_public/$','blog.views.crear_public', name='crear_public'),
                    )
