"""
Accounts admin registers.
"""
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import AdminPasswordChangeForm
from django.utils.translation import gettext_lazy as _

from accounts.models import User
from accounts.forms import UserAdminCreationForm, UserAdminChangeForm


class UserAdmin(BaseUserAdmin):
    """
    User admin.
    """
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm
    change_password_form = AdminPasswordChangeForm
    fieldsets = (
        (_('Personal info'), {'fields': ('phone', 'first_name', 'email')}),
        (_('Permissions'), {'fields': ('is_superuser', 'is_staff')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('phone', 'first_name', 'password1', 'password2'),
        }),
    )

    list_display = ('phone', 'is_active')
    list_filter = ('is_active', 'is_staff')
    search_fields = ('phone', 'name', 'email')
    readonly_fields = ('is_superuser', 'is_staff')


admin.site.register(User, UserAdmin)
