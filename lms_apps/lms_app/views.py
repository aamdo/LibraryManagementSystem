from django.shortcuts import render
from .models import *
from.forms import BookForm

# Create your views here.

def index(request):
    if request.method == 'POST':
        add_book = BookForm(request.POST,request.FILES)
        if add_book.is_valid():
            add_book.save()




    context = {
        'categories':Category.objects.all(),
        'books':Book.objects.all(),
        'form': BookForm(),
        }
    return render(request,'lms/index.html',context)

def books(request):
    context = {
        'categories':Category.objects.all(),
        'books':Book.objects.all(),
        }
    return render(request,'lms/books.html',context)

def delete(request):
    context = {}
    return render(request,'lms/delete.html',context)

def update(request):
    context = {}
    return render(request,'lms/update.html',context)
