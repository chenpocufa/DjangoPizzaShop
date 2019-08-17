from django.contrib import admin
from django.contrib.admin.widgets import RelatedFieldWidgetWrapper
from .models import OrderItem, Order
from django.utils.translation import gettext_lazy as _


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    exclude = ('phone',)
    readonly_fields = ('price',)
    extra = 0

    def formfield_for_dbfield(self, db_field, *args, **kwargs):
        """
        Remove popup add/edit/delete icons by default for relation fields.
        """
        if db_field.is_relation:
            rel = db_field.related_model
            wrapped_widget = RelatedFieldWidgetWrapper(
                db_field.formfield().widget,
                rel,
                admin.site,
                can_add_related=False,
                can_change_related=False,
                can_delete_related=False
            )
            db_field.formfield().widget = wrapped_widget
            return db_field.formfield()
        return super(OrderItemInline, self).formfield_for_dbfield(db_field, **kwargs)


class OrdersAdmin(admin.ModelAdmin):
    list_display = ('created_at', 'delivery_date', 'delivery_time', 'phone', 'name', 'total_price')
    exclude = ('user',)
    inlines = (OrderItemInline,)

    # def _total_price(self):
    #     return sum([item.price for item in self.orderitem_set.all()])

    def total_price(self):
        return sum([item.price for item in self.orderitem_set.all()])

    total_price.short_description = _('Total price')


admin.site.register(Order, OrdersAdmin)
