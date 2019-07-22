from django.contrib import admin
from .models import OrderItem, Order


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    readonly_fields = ('price',)


class OrdersAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'total_price')
    inlines = (OrderItemInline,)


admin.site.register(Order, OrdersAdmin)
