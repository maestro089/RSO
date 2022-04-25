from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class article (models.Model):
    objects = None
    title = models.CharField(max_length=255, verbose_name = "Назване статьи")
    content = models.TextField(blank=True, verbose_name = "Текст статьи")
    photo = models.ImageField(upload_to="photo/%Y/%m/%d/", verbose_name = "Фото")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name = "Дата написания")
    time_update = models.DateTimeField(auto_now=True, verbose_name = "Дата редактирования")
    is_published = models.BooleanField(default=True, verbose_name = "Публикация")
    author = models.ForeignKey(User, null = True, blank = True, verbose_name = "Автор",on_delete = models.CASCADE)


    def __str__(self):
        return self.title


class comments (models.Model):
    object = None
    author = models.ForeignKey(User, null=True, blank=True, verbose_name="Автор", on_delete=models.CASCADE)
    article_name = models.ForeignKey(article,null = True, blank = True, verbose_name="Стаья", on_delete = models.CASCADE)
    message = models.TextField(blank = True, verbose_name="Тескт комментария")


class user_profile(models.Model):
    object = None
    about = models.TextField(blank=True, null = True, verbose_name='Информация о человеке')
    photo = models.ImageField(blank=True, null = True,upload_to="photo_user/%Y/%m/%d/", verbose_name="Фото")
    User = models.ForeignKey(User, null=True, blank=True, verbose_name="Автор", on_delete=models.CASCADE)



