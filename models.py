from typing import Final, final

from django.db import models



@final
class RegUsers(models.Model):
    emailu = models.CharField(max_length=50)
    parol = models.CharField(max_length=30)
    nick = models.CharField(max_length=50)
    date_reg = models.DateField(auto_now_add=True)


class Folders(models.Model):
    num_user = models.ForeignKey(RegUsers, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    release_date = models.DateTimeField(auto_now_add=True)


class Notes(models.Model):
    num_folder = models.ForeignKey(Folders, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    textf = models.TextField()
    filef = models.FileField()
    available = models.BooleanField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
