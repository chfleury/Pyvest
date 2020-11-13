from django.db import models

# Create your models here.
class Investimento(models.Model):
    symbol = models.CharField(max_length = 10)
    name = models.CharField(max_length = 100)
    region = models.CharField(max_length = 100)
    currency = models.CharField(max_length = 20)
    timeOpen = models.CharField(max_length = 20)
    timeClose = models.CharField(max_length = 20)
    timeZone = models.CharField(max_length = 20)
    marketCap = models.FloatField()
    price = models.FloatField()
    changePercent = models.FloatField()
    data = models.CharField(max_length = 100)
    userId = models.IntegerField(default= 0)
