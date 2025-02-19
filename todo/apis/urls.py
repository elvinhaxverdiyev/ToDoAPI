from django.urls import path
from .views import *

urlpatterns = [
    path('todos/', ToDoListCreateAPIView.as_view(), name="todo-list-post"),
    path('todos/<int:pk>/', TodoDetailAPIView.as_view(), name="todo-detail"),
]
