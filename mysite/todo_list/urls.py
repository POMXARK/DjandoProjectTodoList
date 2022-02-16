from django.urls import path

from . import views

app_name = 'todo_list'
app_name = 'todo_list'
urlpatterns = [
    path('', views.IndexViewTodo.as_view(), name='index'),
]