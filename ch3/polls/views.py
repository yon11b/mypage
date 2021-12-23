from django.shortcuts import render

from .models import Info
# Create your views here.

def index(request):
    return render(request,'index.html')

def intro(request): 
    posts=Info.objects.all()
    return render(request,'intro.html',{'posts': posts,})

def context(request):
    posts=Info.objects.all()
    return render(request,'context.html',{'posts': posts,})

