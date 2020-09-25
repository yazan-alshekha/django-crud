from django.db import models
from django.urls import reverse

# Create your models here.
class Users(models.Model):
    title = models.CharField(max_length=64)
    author = models.CharField(max_length=64)
    body = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # return reverse('users')
        return reverse('users_details',args=[str(self.id)])    
