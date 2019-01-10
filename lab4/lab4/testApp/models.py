from __future__ import unicode_literals
from django.db import models


# Create your models here.

class Pictures(models.Model):
    name = models.CharField(max_length=50,)
    description = models.CharField(max_length=1000,)
    place = models.CharField(max_length=30,)

    def __str__(self):
        return ' '.join([self.name, ' in ', self.place, ])
