from django.shortcuts import render
import json
from .models import Plot_Chart


def products(request):
    queryset = Plot_Chart.objects.all()
    names = [obj.name for obj in queryset]
    prices = [int(obj.price) for obj in queryset]

    context = {
        #transforma o objeto python em uma string JSON
        'names': json.dumps(names),
        'prices': json.dumps(prices),
    }
    return render(request, 'plot_chart/products.html', context)