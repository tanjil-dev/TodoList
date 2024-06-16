from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required
from .models import Todo
from .serializers import TodoSerializer

@login_required
@api_view(['GET'])
def todoList(request):
    todo = Todo.objects.filter(user=request.user).order_by('-id')
    serializer = TodoSerializer(todo, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK) 

@login_required
@api_view(['GET'])
def todoSingleDetails(request, pk):
    todo = Todo.objects.get(id=pk)
    serializer = TodoSerializer(todo)
    return Response(serializer.data, status=status.HTTP_200_OK)  

@login_required
@api_view(['POST'])
def todoAdd(request):
    request.data['user'] = request.user.id
    serializer = TodoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)    
    else:
        return Response(serializer.errors, status=status.HTTP_403_FORBIDDEN)

@login_required
@api_view(['POST'])
def todoEdit(request, pk):
    todo = Todo.objects.get(id=pk)
    serializer = TodoSerializer(instance=todo, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)   
    else:
        return Response(serializer.errors, status=status.HTTP_403_FORBIDDEN)

@login_required
@api_view(['DELETE'])
def todoDelete(request, pk):
    todo = Todo.objects.get(id=pk)
    todo.delete()
    return Response('Removed!', status=status.HTTP_200_OK) 