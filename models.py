from typing import Final, final

from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings


@final
def user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.user.id, filename)


class Folders(models.Model):
    num_user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='e-mail', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, default="Доска", verbose_name='Название доски для заметок')
    release_date = models.DateTimeField(auto_now_add=True)


class Notes(models.Model):
    num_folder = models.ForeignKey(Folders, verbose_name='Название папки', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, default="Заметка", verbose_name='Название заметки')
    filen = models.FileField(upload_to=user_directory_path, verbose_name='Загрузить файл')
    textn = models.TextField(verbose_name='Текст заметки')
    urln = models.URLField(verbose_name='Вставить ссылку на объект')
    available = models.BooleanField(verbose_name='Скрыть объект для других пользователей')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
