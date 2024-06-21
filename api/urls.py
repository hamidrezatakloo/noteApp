# api/urls.py

from django.urls import path
from .views import *

urlpatterns = [
    # TodoList endpoints
    path('todolists/', TodoListListCreateView.as_view(), name='todolist_list_create'),
    path('todolists/<int:pk>/', TodoListDetailView.as_view(), name='todolist_detail'),

    # TodoItem endpoints
    path('todolists/<int:list_id>/items/', TodoItemListCreateView.as_view(), name='todoitem_list_create'),
    path('todolists/<int:list_id>/items/<int:pk>/', TodoItemDetailView.as_view(), name='todoitem_detail'),
    path('todolists/<int:list_id>/items/<int:pk>/complete/', TodoItemUpdateStatusView.as_view(), name='todoitem_update_status'),

    # Note endpoints
    path('notes/', NoteListCreateView.as_view(), name='note_list_create'),
    path('notes/<int:pk>/', NoteDetailView.as_view(), name='note_detail'),
]
