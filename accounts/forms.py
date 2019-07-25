"""
Accounts forms.
"""
from django import forms
from django.utils.translation import gettext_lazy as _

from accounts.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class UserAdminCreationForm(UserCreationForm):
    """
    A form for creating new accounts. Includes phone and a repeated password.
    """
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('phone', )
        field_classes = {'phone': forms.CharField}


class UserAdminChangeForm(UserChangeForm):
    """
    A form for updating accounts.

    Includes all the fields on the user, but replaces the password field with admin's password hash display field.
    """
    class Meta:
        model = User
        fields = '__all__'
        field_classes = {'phone': forms.CharField}
