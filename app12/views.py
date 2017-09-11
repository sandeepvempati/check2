from django.shortcuts import render,HttpResponse

# Create your views here.

def hello(request):
    return HttpResponse("Welocme to Django")

def index(request,name):
    return HttpResponse("welcome %s" %name)