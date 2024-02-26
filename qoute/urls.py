# note/urls.py
from django.urls import path
from qoute import views

urlpatterns = [
   path('qoutes/', views.qoute, name='qoutes'),
  
]