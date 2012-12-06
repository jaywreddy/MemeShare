
from django.db import models

class Meme(models.Model):
    meme_id=models.CharField(max_length=255)
    memegroup_id=models.CharField(max_length=255)
    #info...

class MemeGroup(models.Model):
    memegroup_id=models.CharField(max_length=255)
    memegroup_name=models.CharField(max_length=255)
    #info...

class User(models.Model):
    user_id=models.CharField(max_length=255)
    #info...

class user_association(models.Model):
    user_id=models.CharField(max_length=255)
    memegroup_id=models.CharField(max_length=255)
