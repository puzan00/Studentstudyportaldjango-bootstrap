from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Book


@login_required
def book_list(request):
    books = Book.objects.all()
    return render(request, "books.html", {"books": books})


@login_required
def book_detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, "book_detail.html", {"book": book})
