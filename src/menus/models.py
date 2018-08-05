from django.conf import settings
from django.db import models

from restaurants.models import RestaurantLocation

class Item(models.Model):
    user        = models.ForeignKey(settings.AUTH_USER_MODEL)
    restaurant  = models.ForeignKey(RestaurantLocation)
    name        = models.CharField(max_length=120)
    contents    = models.TextField(help_text = 'Separate each item by comma')
    public      = models.BooleanField(default=True)
    timestamp   = models.DateTimeField(auto_now_add=True)
    updated     = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated', '-timestamp']

# Create your models here.
