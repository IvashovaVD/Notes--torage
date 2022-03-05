from typing import Final, final

from django.db import models



@final
class RegUsers(models.Model):
    emailu = models.CharField(max_length=50)
    parol = models.CharField(max_length=30)
    date_reg = models.DateField()


class Folders(models.Model):
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    num_folders_f = models.IntegerField()
    available = models.BooleanField()


class Notes(models.Model):
    num_folder = models.ForeignKey(Folders, on_delete=models.CASCADE)
    num_user = models.ForeignKey(RegUsers, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    textf = models.TextField()
    num_folders_n = models.IntegerField()
    available = models.BooleanField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
