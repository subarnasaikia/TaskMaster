# from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from .models import ToDoList


class ListListView(ListView):
    model = ToDoList
    template_name = "todo_app/index.html"
