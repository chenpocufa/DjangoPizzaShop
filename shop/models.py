from django.db import models
from django.db.models.signals import pre_save
from django.utils.translation import gettext_lazy as _

from catalog.models import Pizza, Size
from accounts.models import User


def check_phone(sender, instance, **kwargs):
    user = User.objects.filter(phone=instance.phone).first()
    if user:
        instance.user = user
    else:
        instance.user = None


class Order(models.Model):
    phone = models.CharField(max_length=100, verbose_name=_('phone'))
    name = models.CharField(max_length=100, verbose_name=_('name'))
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created at'))
    delivery_date = models.DateField(verbose_name=_('delivery date'))
    delivery_time = models.TimeField(verbose_name=_('delivery time'))

    def __str__(self):
        return f""

    class Meta:
        verbose_name = _('order')
        verbose_name_plural = _('orders')

    # def _total_price(self):
    #     return sum([item.price for item in self.orderitem_set.all()])

    @property
    def total_price(self):
        return sum([item.price for item in self.orderitem_set.all()])

    # _total_price.short_description = _('Total price')


pre_save.connect(check_phone, sender=Order)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    item = models.ForeignKey(Pizza, on_delete=models.DO_NOTHING)
    size = models.CharField(max_length=100, choices=Size.CHOICES)
    quantity = models.PositiveSmallIntegerField()

    def __str__(self):
        return f"Item"

    @property
    def price(self):
        return self.item.sizes.get(type=self.size).price * self.quantity