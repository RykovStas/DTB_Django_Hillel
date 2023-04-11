from django.contrib import admin

from .models import Author, Book, Publisher, Store

@admin.register(Author)
class Author(admin.ModelAdmin):
    list_display = ('name', 'age',)
    search_fields = ('name',)
    list_per_page = 20
    ordering = ('id',)
    list_editable = ('age',)


@admin.register(Book)
class Book(admin.ModelAdmin):
    list_display = ('name', 'pages', 'price', 'pubdate',)
    search_fields = ('name',)
    list_filter = ('pubdate',)
    date_hierarchy = 'pubdate'
    list_per_page = 20
    ordering = ('id',)
    list_editable = ('price',)
    readonly_fields = ('pubdate', 'authors')
    fieldsets = (
        ('General Information', {
            'fields': ('name', 'pages', 'price')
        }),
        ('Publication Information', {
            'fields': ('publisher', 'pubdate')
        }),
        ('Authors', {
            'fields': ('authors',)
        }),
    )


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ('name', )
    list_per_page = 20
    ordering = ('id', )


@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ('name', )
    list_per_page = 20
    ordering = ('id', )
    filter_vertical = ('books', )