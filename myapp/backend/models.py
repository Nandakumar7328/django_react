from django.db import models

# Create your models here.
class create_account(models.Model):
    name = models.CharField(max_length=200,default='NA')
    password = models.CharField(max_length=200,default='NA')
    email = models.CharField(max_length=200,default='NA')
    