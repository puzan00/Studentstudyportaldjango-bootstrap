# word_of_the_day/urls.py
from django.urls import path
from news import views

urlpatterns = [
 path('news/', views.news,name='news'),
 
 
]