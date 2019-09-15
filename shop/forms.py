from django import forms
from django.forms import TextInput

from .models import Order
import string
# from django.utils.translation import gettext_lazy as _


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['phone', 'first_name', 'delivery_date', 'delivery_time', 'address', 'comment']

    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        self.fields['phone'].widget = TextInput(attrs={
            'id': 'phone',
            'type': 'phone',
            'class': 'form-control',
            'onsubmit': 'return validationAll()',
            'onchange': 'validatePhone()',
            'placeholder': '+375(xx)xxx-xx-xx'})
        self.fields['first_name'].widget = TextInput(attrs={
            'id': 'first_name',
            'type': 'name',
            'class': 'form-control',
            'oninput': 'validateName()',
            'onsubmit': 'return validationAll()',
            'placeholder': 'Имя'})
        self.fields['delivery_date'].widget = TextInput(attrs={
            'id': 'delivery_date',
            'type': 'text',
            'onchange': 'validateDate()',
            'required pattern': '[0-9_-]*',
            'class': 'form-control datetimepicker-input',
            'data-toggle': 'datetimepicker',
            'data-target': '#delivery_date',
            'placeholder': 'Выберите дату'})
        self.fields['delivery_time'].widget.attrs.update({
            'id': 'delivery_time',
            'onchange': 'validateTime()',
            'class': 'form-control',
            'placeholder': 'Выберите время'})
        self.fields['address'].widget = TextInput(attrs={
            'id': 'address',
            'type': 'text',
            'class': 'form-control',
            'oninput': 'validateAddress()',
            'placeholder': 'Адрес'})
        self.fields['comment'].widget.attrs.update({
            'id': 'comment',
            'class': 'form-control',
            'type': 'textarea',
            'rows': '5'})

    def clean(self):
        phone = self.cleaned_data.get('phone')
        digits = set(string.digits)             # To validate phone
        first_name = self.cleaned_data.get('first_name')
        letters = set(string.ascii_letters)     # To validate name
        '''
        name validation
        '''
        if len(first_name) < 2:
            raise forms.ValidationError('Name is too short')
        for i in first_name:
            if i not in letters:
                raise forms.ValidationError('Only letters in name please')
        '''
        phone validation
        '''
        if len(phone) < 2:
            raise forms.ValidationError('Phone is too short')
        for i in phone:
            if i not in digits:
                raise forms.ValidationError('Only digits in phone please')
