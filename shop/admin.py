from django.contrib import admin
from .models import OrderItem, Order


class OrderItemInline(admin.TabularInline):
    model = OrderItem


class OrdersAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone')
    inlines = (OrderItemInline,)


admin.site.register(Order, OrdersAdmin)
