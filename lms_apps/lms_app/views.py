from django.shortcuts import render
from .models import *

# Create your views here.

def index(request):
    context = {
        'books':Book.objects.all(),
        }
    return render(request,'lms/index.html',context)

def books(request):
    context = {}
    return render(request,'lms/books.html',context)

def delete(request):
    context = {}
    return render(request,'lms/delete.html',context)

def update(request):
    context = {}
    return render(request,'lms/update.html',context)

