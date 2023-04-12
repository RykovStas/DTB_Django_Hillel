from django.db.models import Count, Prefetch
from django.shortcuts import render
from .models import Author, Book, Publisher, Store

def books(request):
    return render(
        request, 'books/book_list.html',
        {'books': Book.objects.select_related('publisher').all()},
    )


def stores(request):
    return render(
        request, 'books/shops_list.html',
        {'stores': Store.objects.annotate(num_books=Count('books')).all()}
    )