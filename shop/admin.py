from django.contrib import admin
from .models import OrderItem, Order


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    readonly_fields = ('price',)
    extra = 0


class OrdersAdmin(admin.ModelAdmin):
    list_display = ('phone', 'name', 'total_price')
    inlines = (OrderItemInline,)


admin.site.register(Order, OrdersAdmin)
