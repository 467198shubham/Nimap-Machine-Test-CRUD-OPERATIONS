from django.db import models

# Create your models here.
class User(models.Model):
    clientname = models.CharField(max_length=100)
    
class Projects(models.Model):
    projectname = models.CharField(max_length=100)
    