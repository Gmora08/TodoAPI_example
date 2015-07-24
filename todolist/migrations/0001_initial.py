# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TodoItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.TextField(verbose_name=b'Item Text')),
            ],
        ),
        migrations.CreateModel(
            name='TodoList',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name=b'List Title')),
                ('author', models.ForeignKey(related_name='todo_list', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='todoitem',
            name='todo_list',
            field=models.ForeignKey(related_name='items', to='todolist.TodoList'),
        ),
    ]
