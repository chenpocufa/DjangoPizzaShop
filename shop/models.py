from django.db import models
from django.db.models.signals import pre_save
from django.utils.translation import gettext_lazy as _, pgettext_lazy

from catalog.models import Pizza, Size
from accounts.models import User


def check_phone(sender, instance, **kwargs):
    user = User.objects.filter(phone=instance.phone).first()
    if user:
        instance.user = user
    else:
        instance.user = None


class Order(models.Model):
    DELIVERY_TIME_CHOICES = [
        (0, '09-10'),
        (1, '10-11'),
        (2, '11-12'),
        (3, '12-13'),
        (4, '13-14'),
        (5, '14-15'),
        (6, '15-16'),
        (7, '16-17'),
        (8, '17-18'),
        (9, '18-18.30'),
    ]
    PAYMENT_CHOICES = [
        (0, _('Cash')),
        (1, _('Card')),
        (2, _('Online')),
    ]
    phone = models.CharField(max_length=100, verbose_name=_('Phone'))
    first_name = models.CharField(max_length=100, verbose_name=pgettext_lazy('Order|Name', 'Order'))
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created at'))
    delivery_date = models.DateField(verbose_name=_('Delivery date'))
    delivery_time = models.SmallIntegerField(
        choices=DELIVERY_TIME_CHOICES,
        verbose_name=_('Delivery time'),
    )
    address = models.CharField(max_length=100, verbose_name=_('Address'))
    comment = models.TextField(max_length=100, verbose_name=_('Comment'), blank=True, null=True)
    payment = models.SmallIntegerField(
        choices=PAYMENT_CHOICES,
        verbose_name=_('Payment method'),
    )
    status = models.BooleanField(default=0, verbose_name=_('Payment confirmed'))

    def total_price(self):
        return sum([item.price for item in self.orderitem_set.all()])

    total_price.short_description = _('Total price')

    def __str__(self):
        return f"№ {self.id}"

    class Meta:
        verbose_name = _('Order')
        verbose_name_plural = _('Orders')


pre_save.connect(check_phone, sender=Order)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name=_('Order'))
    item = models.ForeignKey(Pizza, on_delete=models.DO_NOTHING, verbose_name=_('Item'))
    size = models.CharField(max_length=100, choices=Size.CHOICES, verbose_name=_('Size'))
    quantity = models.PositiveSmallIntegerField(verbose_name=_('Quantity'))

    @property
    def price(self):
        return self.item.sizes.get(type=self.size).price * self.quantity

    "Property admin panel translation"
    def price_admin(self):
        return self.price

    price_admin.short_description = _('Price')

    def __str__(self):
        return f""

    class Meta:
        verbose_name = _("Item")
        verbose_name_plural = _("Items")


class PageTextGroup(models.Model):
    page_name = models.CharField(max_length=100, verbose_name=_('Page name'))
    title = models.CharField(max_length=100, verbose_name=_('Title'))

    def __str__(self):
        return self.page_name

    class Meta:
        verbose_name = _('Page text')
        verbose_name_plural = _('Page texts')


class PageText(models.Model):
    text = models.TextField(max_length=255, verbose_name=_('Text'))
    text_name = models.CharField(max_length=100, blank=True, null=True, verbose_name=_('Text name'))
    group = models.ForeignKey(PageTextGroup, on_delete=models.CASCADE, related_name='texts')

    def __str__(self):
        return f""

    class Meta:
        verbose_name = _('Page text')
        verbose_name_plural = _('Page texts')
