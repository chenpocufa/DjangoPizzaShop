"""
Page views.
"""
import json
from django.shortcuts import render
from catalog.models import Pizza
from .forms import OrderForm


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


def order(request):
    """
    Order form page view.
    """
    template_name = 'shop/order.html'
    if request.method == 'POST':
        # form = OrderForm(request.POST)
        # if form.is_valid():
        #
        data = dict(request.POST)
        order = json.loads(data.pop('order')[0])
        print(order)
        form = OrderForm(data)
        if form.is_valid():
            print('valid')
    else:
        form = OrderForm()
    return render(request, template_name, {'form': form})
