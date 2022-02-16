from django.shortcuts import render

# Create your views here.
from django.views import generic

class IndexViewTodo(generic.ListView):
    template_name = 'todo_list/index.html'
    def get_queryset(self):
        return