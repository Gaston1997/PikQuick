# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response, render, redirect
from blog.models import Entrada
from django.core.mail import EmailMessage

# Create your views here.
def home(request):
    context = RequestContext(request)
    posts = Entrada.objects.filter(published = True)
    return render_to_response('home.html',
                              {'posts':posts},
                              context)

def ver_post(request,id_post):
    context = RequestContext(request)
    mi_post = Entrada.objects.get(id = id_post)
    mensajes = Mensajes.objects.filter(published_in = mi_post, published = True)

    return render_to_response('post.html',
                              {'post':mi_post,
                               'mensajes':mensajes},
                              context)

def nuevapublic(request):
    context = RequestContext(request)
    return render_to_response('nuevapublic.html',
                              context)

def crear_public(request):
    context = RequestContext(request)
    if request.method=='POST':
        pub=Entrada()
        pub.titulo=request.POST['titulo']
        pub.autor=request.POST['autor']
        pub.fecha=request.POST['fecha']
        #pub.descripcion=request.POST['descripcion']
        #pub.archivo=request.FILES['archivo']
        pub.img=request.FILES['img']
        pub.save()

    return render_to_response('nuevapublic.html',
                              context)
