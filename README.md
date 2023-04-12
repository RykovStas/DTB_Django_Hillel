# DTB_Django_Hillel

### ✅ Using prefetch, select, annotation, aggregation minimized queries in the database

>It took me a long time and I had to ask for help

## VIEWS
```python
from django.db.models import Count, Prefetch
from django.shortcuts import render
from .models import Author, Book, Store

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


def authors(request):
    return render(
        request, 'books/authors_list.html',
        {'authors': Author.objects.prefetch_related(Prefetch('book_set', queryset=Book.objects.only('name')))}
    )
```