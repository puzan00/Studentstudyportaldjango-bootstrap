from django.urls import path
from todo import views



urlpatterns = [
    path('todo/', views.todo_list, name='todo'),
    path('todo/new/', views.todo_create, name='todo-create'),
    path('todo/<int:pk>/edit/', views.todo_update, name='todo-update'),
    path('todo/<int:pk>/delete/', views.todo_delete, name='todo-delete'),
    path('todo/complete/<int:pk>/', views.todo_complete, name='todo-complete'),
    path('todo/delete-all',views.todo_delete_all, name='todo-delete-all'),
]
