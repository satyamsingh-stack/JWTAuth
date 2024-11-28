from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    id=models.AutoField(primary_key=True)
    username=models.CharField(max_length=255,unique=True)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=255)

class Blog(models.Model):
    id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=255)
    content=models.TextField(max_length=266)
    author=models.ForeignKey(User, on_delete=models.CASCADE, related_name='u')

