from django.db import models
from django.contrib.auth.models import User

class TodoList(models.Model):
  name = models.CharField('List Title', max_length=200)
  author = models.ForeignKey(User, related_name='todo_list')

class TodoItem(models.Model):
  text = models.TextField('Item Text')
  todo_list = models.ForeignKey(TodoList, related_name='items')


