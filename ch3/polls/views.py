from django.shortcuts import render

from polls.models import Info
# Create your views here.
def intro(request): 
    posts=Info.objects.all()
    return render(request,'intro.html',{'posts': posts,})

def context(request):
    posts=Info.objects.all()
    return render(request,'context.html',{'posts': posts,})

