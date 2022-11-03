from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

# HTTP REQUEST


def home(request):
    return HttpResponse('HOME')


def contato(request):
    return HttpResponse('Contato')


def sobre(request):
    return HttpResponse('sobre')
