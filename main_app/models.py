from django.db import models
from datetime import date
from django.urls import reverse

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=25)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=2)

    def __str__(self):
        return f'{self.name} - {self.address}'

class Post(models.Model):
    item = models.CharField(max_length=50)
    picture = models.CharField(max_length=200)
    description = models.TextField(max_length=250)
    date = models.DateField(default=date.today)
    price = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.item} - {self.date}'
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'post_id': self.id})

class Comment(models.Model):
    content = models.TextField(max_length=150)
    accepted = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.post}'
    def get_absolute_url(self):
        return reverse('detail', kwargs={'post_id': self.post_id})


class Contact(models.Model):
    transaction = models.DateField()
    phone_number = models.CharField(max_length=15)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.comment}'

