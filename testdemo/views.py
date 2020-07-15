from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect,HttpResponse


def index(request):
    return render(request,'index.html')


def upload(request):
    return render(request,'upload.html')


