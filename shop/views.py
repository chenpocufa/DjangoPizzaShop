"""
Page views.
"""
from django.shortcuts import render
from catalog.models import Pizza

pizzas = Pizza.objects.all()


def home(request):
    """
    Home page view.
    """
    template_name = 'shop/home.html'
    context = {
        'pizzas': pizzas
    }
    return render(request, template_name, context)


def about(request):
    """
    About page view.
    """
    template_name = 'shop/about.html'
    return render(request, template_name)


def cart(request):
    """
    Cart page view.
    """
    template_name = 'shop/cart.html'
    return render(request, template_name)
