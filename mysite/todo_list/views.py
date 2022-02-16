from django.shortcuts import render

# Create your views here.
from django.views import generic

class IndexViewTodo(generic.ListView):
    template_name = 'todo_list/index.html'
    #context_object_name = 'main_todo_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return 0