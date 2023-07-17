from django.db import models

# Create your models here.
class Post(models.Model):
    name = models.CharField(max_length=100)
    pic = models.ImageField()
    datetime = models.DateTimeField()
    condition = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    price = models.DecimalField()