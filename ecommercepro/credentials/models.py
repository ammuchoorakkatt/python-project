from django.db import models

# Create your models here.
class User_details(models.Model):
    name=models.CharField(max_length=250,unique=True)
    password=models.SlugField(max_length=250,unique=True)
    def __str__(self):
        return '{}'.format(self.name)