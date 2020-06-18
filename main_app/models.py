from django.db import models
from django.urls import reverse

# Create your models here.
class Game(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    description = models.TextField(max_length=100)
    number = models.IntegerField()

def __str__(self):
    return self.name
    
def get_absolute_url(self):
    return reverse('detail', kwargs={'game_id': self.id})