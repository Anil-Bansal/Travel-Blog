from django.db import models

class User(models.Model):
    username = models.CharField(max_length=70, blank=False, default='')
    password = models.CharField(max_length=200,blank=False, default='')
   

