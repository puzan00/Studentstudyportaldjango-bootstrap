# note/urls.py
from django.urls import path
from note import views

urlpatterns = [
   path('notes/', views.notes, name='notes'),
    path('note-create/', views.note_create, name='note-create'),
    path('note-update/<int:id>/', views.note_update, name='note-update'),
    path('note-delete/<int:id>/', views.note_delete, name='note-delete'),
    
]