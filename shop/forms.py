from django import forms
from django.forms import TextInput, DateInput

from .models import Order
import string
# from django.utils.translation import gettext_lazy as _


class OrderForm(forms.ModelForm):
    phone = forms.CharField(widget=TextInput(attrs={
            'id': 'phone',
            'type': 'phone',
            'class': 'form-control',
            'onsubmit': 'return validationAll()',
            'onchange': 'validatePhone()',
            'placeholder': '+375(xx)xxx-xx-xx'}))
    first_name = forms.CharField(widget=TextInput(attrs={
            'id': 'first_name',
            'type': 'name',
            'class': 'form-control',
            'oninput': 'validateName()',
            'onsubmit': 'return validationAll()',
            'placeholder': 'Имя'}))
    delivery_date = forms.DateField(widget=DateInput(attrs={
            'id': 'delivery_date',
            'type': 'text',
            'onchange': 'validateDate()',
            'autocomplete': 'off',
            'required pattern': '[0-9_-]*',
            'class': 'form-control datetimepicker-input',
            'data-toggle': 'datetimepicker',
            'data-target': '#delivery_date',
            'placeholder': 'Выберите дату'}))
    # delivery_time = forms.IntegerField(widget=IntegerField(attrs={
    #         'id': 'delivery_time',
    #         'onchange': 'validateTime()',
    #         'class': 'form-control',
    #         'placeholder': 'Выберите время'}))
    address = forms.CharField(widget=TextInput(attrs={
            'id': 'address',
            'type': 'text',
            'class': 'form-control',
            'oninput': 'validateAddress()',
            'placeholder': 'Адрес'}))
    comment = forms.CharField(widget=TextInput(attrs={
            'id': 'comment',
            'class': 'form-control',
            'type': 'textarea',
            'size': '40',
            'rows': '5'}), required=False)

    class Meta:
        model = Order
        fields = ['phone', 'first_name', 'delivery_date', 'delivery_time', 'address', 'payment', 'comment']

    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        self.fields['delivery_time'].widget.attrs.update({
                'id': 'delivery_time',
                'onchange': 'validateTime()',
                'class': 'form-control',
                'placeholder': 'Выберите время'})
        self.fields['payment'].widget.attrs.update({
                'id': 'payment',
                'onchange': 'validatePaymentWay()',
                'class': 'form-control',
                'placeholder': 'Выберите способ оплаты'})

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
