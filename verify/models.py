from django.db import models

# Create your models here.
class Aza(models.Model):
    number = models.CharField(max_length=500)
    code = models.CharField(max_length=3)
    name = models.CharField(max_length=500)