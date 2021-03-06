from django.shortcuts import redirect, render
from .models import *
from.forms import BookForm,CategoryForm

# Create your views here.

def index(request):
    if request.method == 'POST':
        add_book = BookForm(request.POST,request.FILES)
        if add_book.is_valid():
            add_book.save()

        add_cat = CategoryForm(request.POST)
        if add_cat.is_valid():
            add_cat.save()

    context = {
        'categories':Category.objects.all(),
        'books':Book.objects.all(),
        'Bform': BookForm(),
        'Cform': CategoryForm(),
        'allbooks':Book.objects.filter(active=True).count(),
        'booksold':Book.objects.filter(status='sold').count(),
        'bookrented':Book.objects.filter(status='rented').count(),
        'bookavailble':Book.objects.filter(status='availble').count(),
        }
    return render(request,'lms/index.html',context)

def books(request):
    search=Book.objects.all()
    title = None
    if 'search_name' in request.GET:
        title = request.GET['search_name']
        if title:
            search = search.filter(title__icontains=title)


    context = { 
        'categories':Category.objects.all(),
        'books':search,
        'Cform': CategoryForm(),
        }
    return render(request,'lms/books.html',context)


def update_book(request,id):
    book = Book.objects.get(id=id)
    if request.method == 'POST':
        book_new = BookForm(request.POST,request.FILES,instance=book)
        if book_new.is_valid():
            book_new.save()
            return redirect('/')
    else:
        book_info = BookForm(instance=book)
                 
    context = {
        'book':book_info,
        }
    return render(request,'lms/update.html',context)


def delete_book(request,id):
    book = Book.objects.get(id=id)
    if request.method == 'POST':
        book.delete()
        return redirect('/')

    
    return render(request,'lms/delete.html')
