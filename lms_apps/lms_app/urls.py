from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index ,name='index'),
    path('books/',views.books ,name='books'),
    path('update_book/<int:id>',views.update_book ,name='update_book'),
    path('delete_book/<int:id>',views.delete_book ,name='delete_book'),
]