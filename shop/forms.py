from django import forms
from .models import Order


# class OrderForm(forms.Form):
#     name = forms.CharField(label='Your name ', max_length=100)
#     phone = forms.CharField(label='Your phone # ', max_length=10)


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['name', 'phone']
