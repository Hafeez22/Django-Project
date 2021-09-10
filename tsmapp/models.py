from typing import Text
from django.db import models
from django.db.models.fields import CharField, EmailField, IntegerField

# Create your models here.
class tsm(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    phone = models.CharField(max_length=13)
    text = models.CharField(max_length=100)
    
class items(models.Model):
    img = models.ImageField(upload_to='pics')
    namei = models.CharField(max_length=30)
    desc = models.CharField(max_length=100)

class review(models.Model):
    img = models.ImageField(upload_to='pics')
    name = models.CharField(max_length=30)
    head = models.CharField(max_length=30)
    revi = models.CharField(max_length=300)

class firstreview(models.Model):
    imagef = models.ImageField(upload_to='pics')    
    namef = models.CharField(max_length=30)
    headf = models.CharField(max_length=50)
    revif = models.CharField(max_length=100)