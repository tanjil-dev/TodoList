from django.contrib.auth.models import Group, User
from todoApi.serializers import GroupSerializer, UserSerializer
from rest_framework import permissions, viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Todo
from .serializers import TodoSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


@api_view(['GET'])
def todoList(request):
    todo = Todo.objects.all()
    serializer = TodoSerializer(todo, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK) 

@api_view(['GET'])
def todoSingleDetails(request, pk):
    todo = Todo.objects.get(id=pk)
    serializer = TodoSerializer(todo)
    return Response(serializer.data, status=status.HTTP_200_OK)  

@api_view(['POST'])
def todoAdd(request):
    serializer = TodoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)    
    else:
        return Response(serializer.errors, status=status.HTTP_403_FORBIDDEN)
    
@api_view(['PUT'])
def todoEdit(request, pk):
    todo = Todo.objects.get(id=pk)
    serializer = TodoSerializer(instance=todo, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)   
    else:
        return Response(serializer.errors, status=status.HTTP_403_FORBIDDEN)

@api_view(['DELETE'])
def todoDelete(request, pk):
    todo = Todo.objects.get(id=pk)
    todo.delete()
    return Response('Removed!', status=status.HTTP_200_OK) 