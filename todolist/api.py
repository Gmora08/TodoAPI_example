from tastypie.resources import ModelResource
from tastypie.serializers import Serializer
from .models import TodoList, TodoItem

class TodoListResource(ModelResource):
  class Meta:
    queryset = TodoList.objects.all()
    resource_name = 'lists'
    serializer = Serializer(formats=['json',])

class TodoItemResource(ModelResource):
  class Meta:
    queryset = TodoItem.objects.all()
    resource_name = 'items'
    serializer = Serializer(formats=['json',])
