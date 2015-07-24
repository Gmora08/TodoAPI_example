from tastypie.resources import ModelResource
from .models import TodoList, TodoItem

class TodoListResource(ModelResource):
  class Meta:
    queryset = TodoList.objects.all()
    resource_name = 'lists'

class TodoItemResource(ModelResource):
  class Meta:
    queryset = TodoItem.objects.all()
    resource_name = 'items'
