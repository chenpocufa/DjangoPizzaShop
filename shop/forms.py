from django import forms
from .models import Order
import string
# from django.utils.translation import gettext_lazy as _


class OrderForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['phone'].widget.attrs.update({'class': 'form-control', 'type': 'phone', 'placeholder': '(xx)xx-xx-xx'})
        self.fields['name'].widget.attrs.update({'class': 'form-control is-valid', 'type': 'text', 'placeholder': 'Имя'})
    #   self.fields['delivery_date'].widget.attrs.update({'class': 'form-control datetimepicker-input', 'type': 'text', 'id': 'datetimepicker9', 'placeholder': 'Дата доставки', 'data-toggle': 'datetimepicker', 'data-target': '#datetimepicker9'})
        self.fields['delivery_time'].widget.attrs.update({'class': 'form-control', 'type': '', 'placeholder': 'Время доставки'})
        self.fields['address'].widget.attrs.update({'class': 'form-control', 'type': 'text', 'placeholder': 'Адрес'})
        self.fields['comment'].widget.attrs.update({'class': 'form-control', 'type': 'text', 'rows': '5', 'placeholder': 'Комментарий'})

    class Meta:
        model = Order
        fields = ['phone', 'name', 'delivery_date', 'delivery_time', 'address', 'comment']

    def clean(self):
        phone = self.cleaned_data.get('phone')
        digits = set(string.digits)             # To validate phone
        name = self.cleaned_data.get('name')
        letters = set(string.ascii_letters)     # To validate name
        '''
        name validation
        '''
        if len(name) < 2:
            raise forms.ValidationError('Name too short')
        for i in name:
            if i not in letters:
                raise forms.ValidationError('Only letters in name please')
        '''
        phone validation
        '''
        if len(phone) < 2:
            raise forms.ValidationError('Phone too short')
        for i in phone:
            if i not in digits:
                raise forms.ValidationError('Only digits in phone please')
