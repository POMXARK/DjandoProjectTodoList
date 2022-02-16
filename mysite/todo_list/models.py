from django.db import models

# Create your models here.


class TodoAction(models.Model):
    todo_text = models.CharField(max_length=200)