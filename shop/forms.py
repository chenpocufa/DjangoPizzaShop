from django import forms


class OrderForm(forms.Form):
    name = forms.CharField(label='Your name ', max_length=100)
    phone = forms.CharField(label='Your phone number ', max_length=10, required=True)
    # payment = forms.ChoiceField
