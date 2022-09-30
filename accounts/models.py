import email
from django.db import models


class User(models.Model):
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    password = models.CharField(max_length=50)
    #photo = models.ImageField(blank=False)

    def __str__(self):
        return self.username

# Create your models here.
