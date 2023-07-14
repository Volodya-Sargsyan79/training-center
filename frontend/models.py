from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Teachers(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=20)
    date = models.DateField()
    image = models.ImageField(upload_to="teacher_img")
    email = models.EmailField(max_length=50, primary_key=True)
    user_name = models.CharField(max_length=10)
    password = models.CharField(max_length=250)



class Students(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=20)
    date = models.DateField()
    image = models.ImageField(upload_to="teacher_img")
    email = models.EmailField(max_length=50, primary_key=True)
    user_name = models.CharField(max_length=10)
    password = models.CharField(max_length=250)