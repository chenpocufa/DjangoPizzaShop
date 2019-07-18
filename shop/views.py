"""
Page views.
"""
import json
from django.shortcuts import render, redirect
from catalog.models import Pizza
from .models import OrderItem, Order
from .forms import OrderForm
from django.contrib import messages


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
    if request.method == 'POST':
        form_content = request.POST.copy()
        order_content = json.loads(form_content.pop('order')[0])
        form = OrderForm(form_content)

        if form.is_valid():
            form = form.save()
            messages.success(request, f'Thank you!')

            # create object OrderItem item for each item in the order
            for i in order_content.items():
                order_item = i[1]
                item = Pizza.objects.get(id=order_item['id'])
                item_price_check = 'none'
                if order_item['size'] == 'small':
                    item_price_check = item.order(['price_small'])['price_small']
                elif order_item['size'] == 'large':
                    item_price_check = item.order(['price_large'])['price_large']
                params = dict(
                    user_form=form,
                    item_name=item.order(['name'])['name'],
                    item_price=item_price_check,
                    size=order_item['size'],
                    quantity=order_item['quantity'],
                )
                OrderItem.objects.create(**params)

    else:
        form = OrderForm()
    return render(request, 'shop/order.html', {'form': form})
