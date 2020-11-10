from django.db import models

# Create your models here.
class Form_Info(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255,blank=True)
    ico = models.CharField(max_length=8)