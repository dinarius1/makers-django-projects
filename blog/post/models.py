from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model() #создали класс Пользователь


class Post(models.Model): #models - это файл, где есть класс Model
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts') #этот режим говорит,что если удаляется юзер, то удаляется вся таблица
    # related_name= - 
    title = models.CharField(max_length=100)  #CharField - тип данных строка, тоже класс
    body = models.TextField(blank=True, null=True) #blank=True, null=True - делает данное поля необязательным для заполнения
    created_at = models.DateTimeField(auto_now_add=True) #позволяет создавать дату автоматически


