from django import forms
from django.forms import TextInput, DateInput

from .models import Order
from timetable.models import Date


class OrderForm(forms.ModelForm):
    phone = forms.CharField(widget=TextInput(attrs={
            'id': 'phone',
            'type': 'phone',
            'class': 'form-control',
            'onsubmit': 'return validationAll()',
            'onchange': 'validatePhone()',
            'placeholder': '(xx)xxx-xx-xx'}))
    first_name = forms.CharField(widget=TextInput(attrs={
            'id': 'first_name',
            'type': 'name',
            'class': 'form-control',
            'oninput': 'validateName()',
            'onsubmit': 'return validationAll()',
            'placeholder': 'Имя'}))

    dates = Date.objects.all()
    dates_list = []
    for d in dates:
        date = str(d).replace('-', '/')
        dates_list.append(date)
    print(dates_list)
    delivery_date = forms.DateField(widget=DateInput(attrs={
            'id': 'delivery_date',
            'type': 'text',
            'onchange': 'validateDate()',
            'autocomplete': 'off',
            'required pattern': '[0-9_-]*',
            'class': 'form-control datetimepicker-input',
            'data-toggle': 'datetimepicker',
            'data-target': '#delivery_date',
            'placeholder': 'Выберите дату',
            'dates': dates_list}))
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
