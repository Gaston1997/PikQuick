# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response, render, redirect
#from blog.models import Entrada
from django.core.mail import EmailMessage

# Create your views here.
def home(request):
    context = RequestContext(request)
    #posts = Entrada.objects.filter(published = True)
    return render_to_response('home.html',
                              {},
                              context)
