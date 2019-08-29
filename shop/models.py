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
        ('9-10', '9-10'),
        ('10-11', '10-11'),
        ('11-12', '11-12'),
        ('12-13', '12-13'),
        ('13-14', '13-14'),
        ('14-15', '14-15'),
        ('15-16', '15-16'),
        ('16-17', '16-17'),
        ('17-18', '17-18'),
        ('18-18.30', '18-18.30'),
    ]
    phone = models.CharField(max_length=100, verbose_name=_('Phone'))
    name = models.CharField(max_length=100, verbose_name=_('Name'))
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created at'))
    delivery_date = models.DateField(verbose_name=_('Delivery date'))
    delivery_time = models.CharField(
        max_length=10,
        choices=DELIVERY_TIME_CHOICES,
        verbose_name=_('Delivery time')
    )
    address = models.CharField(max_length=100, verbose_name=_('Address'))
    comment = models.CharField(max_length=100, verbose_name=_('Comment'), blank=True, null=True)

    def __str__(self):
        return f""

    class Meta:
        verbose_name = _('order')
        verbose_name_plural = _('orders')

    @property
    def total_price(self):
        return sum([item.price for item in self.orderitem_set.all()])


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


class PageTextGroup(models.Model):
    page_name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.page_name


class PageText(models.Model):
    text = models.TextField(max_length=255)
    text_name = models.CharField(max_length=100, blank=True, null=True)
    group = models.ForeignKey(PageTextGroup, on_delete=models.CASCADE, related_name='texts')

    def __str__(self):
        return f"Page text"
