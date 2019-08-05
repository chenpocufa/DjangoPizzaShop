"""
Accounts admin registers.
"""
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import AdminPasswordChangeForm
from django.forms.models import BaseInlineFormSet
from django.utils.translation import gettext_lazy as _
# from django.urls import reverse

from accounts.models import User
from accounts.forms import UserAdminCreationForm, UserAdminChangeForm
from shop.models import Order


class UserOrders(BaseInlineFormSet):
    def __init__(self, *args, **qwargs):
        super(UserOrders, self).__init__(*args, **qwargs)
        user = qwargs['instance']
        self.queryset = Order.objects.filter(phone=user.phone)


class OrderInline(admin.TabularInline):
    model = Order
    formset = UserOrders
    extra = 0
    show_change_link = True
    readonly_fields = ('name', 'phone', 'total_price')

    # def link(self, obj):
    #     url = reverse('admin:%s_%s_change' % (obj._meta.app_label, obj._meta.model_name), args=[obj.id])
    #     print(url)
    #     return 'http://localhost%s' % url

    def has_add_permission(self, request):
        return False


class UserAdmin(BaseUserAdmin):
    """
    User admin.
    """
    form = UserAdminChangeForm
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

    list_display = ('phone', 'first_name', 'is_active')
    list_filter = ('is_active', 'is_staff')
    search_fields = ('phone', 'name', 'email')
    readonly_fields = ('is_superuser', 'is_staff')

    inlines = (OrderInline,)


admin.site.register(User, UserAdmin)
