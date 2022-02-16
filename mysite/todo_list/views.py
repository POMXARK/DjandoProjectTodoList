from django.shortcuts import render

# Create your views here.
from django.views import generic

from .models import TodoAction


class IndexViewTodo(generic.ListView):
    model = TodoAction
    template_name = 'todo_list/index.html'
    context_object_name = 'todo_actions'
    #def get_queryset(self):
    #    return