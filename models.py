from typing import Final, final

from django.db import models



@final
def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT / user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id, filename)


class RegUsers(models.Model):
    emailu = models.CharField(max_length=50)
    parol = models.CharField(max_length=30)
    nick = models.CharField(max_length=50)
    date_reg = models.DateField(auto_now_add=True)


class Folders(models.Model):
    num_user = models.ForeignKey(RegUsers, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, default="Доска")
    release_date = models.DateTimeField(auto_now_add=True)


class Notes(models.Model):
    num_folder = models.ForeignKey(Folders, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, default="Заметка")
    filen = models.FileField(upload_to=user_directory_path)
    textn = models.TextField()
    urln = models.URLField()
    available = models.BooleanField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
