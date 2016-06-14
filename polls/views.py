from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
  return HttpResponse('Hellp, World. You are at the polls index')

def test(request):
  return HttpResponse('Hellp, again test')