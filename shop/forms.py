from django import forms
from .models import Order
import string
# from django.utils.translation import gettext_lazy as _


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['phone', 'first_name', 'delivery_date', 'delivery_time', 'address', 'comment']

    def clean(self):
        phone = self.cleaned_data.get('phone')
        digits = set(string.digits)             # To validate phone
        first_name = self.cleaned_data.get('first_name')
        letters = set(string.ascii_letters)     # To validate name
        address = self.cleaned_data.get('address')
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
        '''
        address validation
        '''
        if len(phone) < 5:
            raise forms.ValidationError('Address is too short')
