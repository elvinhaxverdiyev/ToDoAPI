from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from todoapp.models import ToDo
from todoapp.serializers import ToDoSerializer
# Create your views here.

class ToDoListCreateAPIView(APIView):
    """
    This view handles both the listing of all ToDo items 
    and creating new ToDo items.

    GET:
        Returns a list of all ToDo items.

    POST:
        Creates a new ToDo item.
        Expects data in the form of title, text, and is_complate.
    """
    def get(self, request):
        """
        List all ToDo items.
        """
        todos = ToDo.objects.all()
        serializer = ToDoSerializer(todos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        """
        Create a new ToDo item.
        """
        serializer = ToDoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class TodoDetailAPIView(APIView):
    """
    This view provides operations on a single ToDo item.
    It supports retrieving, updating, and deleting a specific ToDo.

    GET:
        Retrieves a specific ToDo item by its ID (pk).
    
    PATCH:
        Partially updates a specific ToDo item by its ID (pk).
    
    DELETE:
        Deletes a specific ToDo item by its ID (pk).
    """
    def get_todo(self, pk):
        """
        Retrieves a ToDo item by its primary key (pk).
        If the ToDo does not exist, it raises a 404 error.
        """
        return get_object_or_404(ToDo, pk=pk)
        
    def get(self, request, pk):
        """
        Get the details of a specific ToDo item by its ID.
        """
        todo = self.get_todo(pk)
        serializer = ToDoSerializer(todo)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def patch(self, request, pk):
        """
        Partially update a specific ToDo item by its ID.
        Only the provided fields will be updated.
        """
        todo = self.get_todo(pk)
        serializer = ToDoSerializer(todo, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        """
        Delete a specific ToDo item by its ID.
        """
        todo = self.get_todo(pk)
        todo.delete()
        return Response({"message": "ToDo successfully deleted!"}, status=status.HTTP_204_NO_CONTENT)

        