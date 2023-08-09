from django.contrib import admin
#Admin@123456
# Register your models here.
from todo_app.models import ToDoItem, ToDoList

admin.site.register(ToDoItem)
admin.site.register(ToDoList)
