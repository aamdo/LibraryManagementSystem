from tkinter.constants import PAGES

from django.db import models
from django.db.models.deletion import PROTECT
from django.db.models.fields import DecimalField


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Book(models.Model):

    book_status = {
        ('availble', 'availble'),
        ('rented', 'rented'),
        ('sold', 'sold'),
    }

    title = models.CharField(max_length=250)
    author = models.CharField(max_length=250, blank=True, null=True)
    photo_book = models.ImageField(upload_to='photo', blank=True, null=True)
    photo_author = models.ImageField(upload_to='photo', blank=True, null=True)
    pages = models.IntegerField(blank=True, null=True)
    price = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, null=True)
    rental_price_day = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, null=True)
    rental_period = models.IntegerField(blank=True, null=True)
    total_rental = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    status = models.CharField(
        max_length=50, choices=book_status, blank=True, null=True)
    category = models.ForeignKey(
        Category, on_delete=PROTECT, blank=True, null=True)

    def __str__(self):
        return self.title
