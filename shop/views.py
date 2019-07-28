"""
Page views.
"""
import json

from django.shortcuts import render, redirect
from django.contrib import messages
# from django.contrib.auth import login, authenticate

from .models import OrderItem
from .forms import OrderForm

from catalog.models import Pizza
from accounts.forms import UserCreationForm, UserChangeForm


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
            for order_item in order_content:
                item = Pizza.objects.get(id=order_item['id'])
                params = dict(
                    user_form=form,
                    item=item,
                    size=order_item['size'],
                    quantity=order_item['quantity'],
                )
                OrderItem.objects.create(**params)

    else:
        form = OrderForm()
    return render(request, 'shop/order.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, f'You can log in now')
            # phone = form('phone')
            # raw_password = form.cleaned_data.get('password1')
            # user = authenticate(phone=phone, password=raw_password)
            # login(request, user)
            return redirect('shop-home')

    else:
        form = UserCreationForm()
    return render(request, 'shop/registration.html', {'form': form})
