"""
Accounts admin registers.
"""
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import AdminPasswordChangeForm
from django.utils.translation import gettext_lazy as _

from accounts.models import User
from accounts.forms import UserAdminCreationForm, UserAdminChangeForm
from django.forms.models import BaseInlineFormSet
from shop.models import Order


class UserOrders(BaseInlineFormSet):

    def __init__(self, *args, **qwargs):
        super(UserOrders, self).__init__(*args, **qwargs)
        # user = qwargs['instance']
        print(qwargs)
        self.queryset = Order.objects.all()
    # OrderFormSet = modelformset_factory(Order, fields=('name',))


class OrderInline(admin.TabularInline):
    model = Order
    formset = UserOrders
    extra = 1
    show_change_link = True


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

    inlines = (OrderInline,)


admin.site.register(User, UserAdmin)
