from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Todo
from .serializers import TodoSerializer
from django.shortcuts import render, redirect


def todo_list_view(request):
    todos = Todo.objects.all()  
    return render(request, 'todos/todo_list.html', {'todos': todos})


@api_view(['GET'])
def api_todo_list(request):
    todos = Todo.objects.all()
    serializer = TodoSerializer(todos, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def api_create_todo(request):
    if request.content_type == 'application/x-www-form-urlencoded':
        title = request.POST.get('title')
        description = request.POST.get('description')
        completed = request.POST.get('completed') == 'on'
        todo = Todo(title=title, description=description, completed=completed)
        todo.save()
        return redirect('todo_list')  
    else:
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST', 'PUT'])
def api_update_todo(request, id):
    todo = get_object_or_404(Todo, id=id)
    if request.content_type == 'application/x-www-form-urlencoded':
        title = request.POST.get('title')
        description = request.POST.get('description')
        completed = request.POST.get('completed') == 'on'
        todo.title = title
        todo.description = description
        todo.completed = completed
        todo.save()
        return redirect('todo_list') 
    else:
        serializer = TodoSerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST', 'DELETE'])
def api_delete_todo(request, id):
    todo = get_object_or_404(Todo, id=id)
    if request.method == 'POST':
        todo.delete()
        return redirect('todo_list') 
    else:
        return Response(status=status.HTTP_204_NO_CONTENT)

def todo_form(request, id=None):
    todo = None
    if id:
        todo = get_object_or_404(Todo, id=id)
    return render(request, 'todos/todo_form.html', {'todo': todo})
