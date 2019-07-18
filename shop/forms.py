from django import forms
from .models import Order
import string


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['name', 'phone']

    def clean(self):
        name = self.cleaned_data.get('name')
        letters = set(string.ascii_letters)     # To validate name
        phone = self.cleaned_data.get('phone')
        digits = set(string.digits)     # To validate phone
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
