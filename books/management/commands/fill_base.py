import random
from django.core.management.base import BaseCommand
from faker import Faker
from books.models import Author, Publisher, Book, Store


class Command(BaseCommand):
    help = 'Populates the database'

    def handle(self, *args, **options):
        fake = Faker()

        publishers = []
        for publisher in range(100):
            publisher = Publisher.objects.create(name=fake.company())
            publishers.append(publisher)

        authors = []
        for author in range(500):
            author = Author.objects.create(name=fake.name(), age=random.randint(18, 80))
            authors.append(author)

        books = []
        for book in range(1000):
            book = Book.objects.create(
                name=fake.text(max_nb_chars=50),
                pages=random.randint(50, 1000),
                price=random.uniform(10, 100),
                rating=random.uniform(1, 5),
                publisher=random.choice(publishers),
                pubdate=fake.date_between(start_date='-5y', end_date='today')
            )
            book.authors.add(*random.sample(authors, random.randint(1, 3)))
            books.append(book)

        stores = []
        for store in range(10):
            store = Store.objects.create(name=fake.company())
            store.books.add(*random.sample(books, random.randint(10, 200)))
            stores.append(store)
