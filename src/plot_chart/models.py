from django.db import models
from __future__ import unicode_literals

#cria o modelo, cada atributo do modelo representa um campo do banco de dados    
class Plot_Chart(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=9, decimal_places=2)

    def __str__(self):
        return self.name