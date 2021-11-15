from django.shortcuts import render
from django.views.generic import ListView, DetailView

from books.models import Book


def index_view(request):
    return render(request=request,
                  template_name='books/index.html')


class BookList(ListView):
    model = Book


class BookDetail(DetailView):
    model = Book