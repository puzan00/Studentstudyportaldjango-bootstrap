from django.urls import path
from . import views

urlpatterns = [
    path("books/", views.book_list, name="book-list"),
    path("book/<int:book_id>/", views.book_detail, name="book-detail"),
]
