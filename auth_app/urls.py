# auth_app/urls.py
from django.urls import path
from auth_app import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.signin, name='login'),
    path('logout/', views.signout, name='logout'),  
]
