from django.db import models

# Create your models here.
class User(models.Model):
    clientname = models.CharField(max_length=100)
    