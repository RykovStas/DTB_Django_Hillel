from django.shortcuts import render
from .models import Book

def index(request):
    return render(
        request, 'books/book_list.html',
        {'books': Book.objects.select_related('publisher').all()},
    )
