from django.http import HttpResponse
from django.shortcuts import HttpResponseRedirect, redirect, render
from django.template import loader
from django.urls import reverse
from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request,'index.html')
    #return HttpResponse("Hello World")
def login(request):
    context={}
    #return render(request,'index.html',context)
    #return HttpResponse('index.html')
    #return HttpResponseRedirect(reverse('index.html'))
    #return redirect('index')
    return HttpResponseRedirect(reverse('index'))
def signup(request):
    return render(request,'signup.html')
    
    