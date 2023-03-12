from django.shortcuts import render
import json

from books.models import Book


def books_view(request):
    template = 'books/books_list.html'
    context = {}
    return render(request, template, context)


def date_view(request, pub_date):
    template = 'books/date.html'
    # with open('fixtures/books.json', 'r') as f:
    #     context = json.load(f)
    date_context = Book.objects.get(pub_date=pub_date)
    return render(request, template, context)
