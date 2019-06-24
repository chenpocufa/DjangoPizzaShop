from django.shortcuts import render
from catalog.models import Pizza

pizzas = Pizza.objects.all()


def home(request):
    context = {
        'pizzas': pizzas
    }
    return render(request, 'shop/home.html', context)


def about(request):
    return render(request, 'shop/about.html')
