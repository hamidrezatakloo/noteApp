from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.models import TodoItem, Note, TodoList
from api.serializers import TodoItemSerializer, NoteSerializer, TodoListSerializer


# TodoList views
class TodoListListCreateView(generics.ListCreateAPIView):
    queryset = TodoList.objects.all()
    serializer_class = TodoListSerializer


class TodoListDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TodoList.objects.all()
    serializer_class = TodoListSerializer


# TodoItem views
class TodoItemListCreateView(generics.ListCreateAPIView):
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer

    def get_queryset(self):
        return TodoItem.objects.filter(todo_list_id=self.kwargs['list_id'])

    def perform_create(self, serializer):
        serializer.save(todo_list_id=self.kwargs['list_id'])


class TodoItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer


class NoteListCreateView(generics.ListCreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer


class NoteDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer


class TodoItemUpdateStatusView(APIView):
    def post(self, request, list_id, pk):
        try:
            todo_item = TodoItem.objects.get(pk=pk, todo_list_id=list_id)
        except TodoItem.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        todo_item.completed = True
        todo_item.save()

        serializer = TodoItemSerializer(todo_item)
        return Response(serializer.data, status=status.HTTP_200_OK)
