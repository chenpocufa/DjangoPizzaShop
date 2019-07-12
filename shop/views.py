"""
Page views.
"""
import json
from django.shortcuts import render, redirect
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


# def order(request):
#     """
#     Order form page view.
#     """
#     template_name = 'shop/order.html'
#     if request.method == 'POST':
#         data = dict(request.POST)
#         order = json.loads(data.pop('order')[0])
#         print(order)
#         form = OrderForm()
#         if form.is_valid():
#             print('valid')
#     else:
#         form = OrderForm()
#     return render(request, template_name, {'form': form})

def order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('shop-home')
    else:
        form = OrderForm()
    return render(request, 'shop/order.html', {"form": form})
