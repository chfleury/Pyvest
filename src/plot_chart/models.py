from django.db import models

# Create your models here.

from __future__ import unicode_literals

class Plot_Chart(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=9, decimal_places=2)

    def __str__(self):
        return self.name