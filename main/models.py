from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ToDoList(models.Model):
    title = models.CharField(max_length=200)
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,related_name="todolist")

    def __str__(self):
        return self.title

class Item(models.Model):
    text = models.CharField(max_length=300)
    list = models.ForeignKey(ToDoList,on_delete=models.CASCADE)
    complete = models.BooleanField(default=False)