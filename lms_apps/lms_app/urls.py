from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index ,name='index'),
    path('books/',views.index ,name='books'),
    path('delete/',views.index ,name='delete'),
    path('update/',views.index ,name='update'),
    
]