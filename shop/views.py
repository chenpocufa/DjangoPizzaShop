"""
Page views.
"""
import json

from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.db import transaction
from django.shortcuts import render, redirect
from django.urls import reverse

from .models import OrderItem
from .forms import OrderForm

from catalog.models import Pizza
from accounts.models import User
from accounts.forms import UserCreationForm
from .models import Order
from .models import PageTextGroup
from timetable.models import Date


def home(request):
    """
    Home page view.
    """
    template_name = 'shop/home.html'
    pizzas = Pizza.objects.all()
    context = {
        'pizzas': pizzas
    }
    return render(request, template_name, context)


def about(request):
    """
    About page view.
    """
    template_name = 'shop/about.html'
    path = request.path.strip('/')
    text_group = PageTextGroup.objects.filter(page_name=path).first()
    if text_group is None:
        context = {'text': text_group}
    else:
        variables = [(text.text_name, text.text) for text in text_group.texts.all()]
        context = {'text': text_group, **dict(variables)}
    return render(request, template_name, context)


def cart(request):
    """
    Cart page view.
    """
    template_name = 'shop/cart.html'
    pizzas = Pizza.objects.all()
    context = {
        'pizzas': pizzas
    }
    return render(request, template_name, context)


def profile(request):
    """
    User profile page view.
    """
    template_name = 'shop/profile.html'

    if not request.user.is_authenticated:
        return redirect(reverse('login'))

    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('shop-home')
        else:
            messages.error(request, f'Please correct errors {form.errors}.')
    else:
        form = PasswordChangeForm(request.user)

    user = User.objects.get(phone=request.user.phone)
    context = {
        'orders': Order.objects.filter(phone=user.phone),
        'form': form
    }

    return render(request, template_name, context)


def order(request):
    form = OrderForm(data=request.POST)
    if request.method == 'POST':
        mutable_request_data = request.POST.copy()
        order_items = json.loads(mutable_request_data.pop('order')[0])
        order_details = OrderForm(mutable_request_data)
        print(mutable_request_data)

        if order_details.is_valid():

            with transaction.atomic():
                order_obj = order_details.save()

                # create object OrderItem item for each item in the order
                for order_item in order_items:
                    item = Pizza.objects.get(id=order_item['id'])
                    params = dict(
                        order=order_obj,
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
            return redirect('shop-home')

    else:
        form = UserCreationForm()
    return render(request, 'shop/registration.html', {'form': form})


def timetable(request):
    """
    Timetable page view.
    """
    template_name = 'shop/timetable.html'
    dates = Date.objects.all()
    context = {
        'dates': dates
    }
    return render(request, template_name, context)
