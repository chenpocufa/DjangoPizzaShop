from django.db import models
from django.db.models.signals import pre_save

from catalog.models import Pizza, Size
from accounts.models import User


def check_phone(sender, instance, **kwargs):
    user = User.objects.filter(phone=instance.phone).first()
    if user:
        instance.user = user
    else:
        instance.user = None


class Order(models.Model):
    phone = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True, null=True)

    def __str__(self):
        return f""

    @property
    def total_price(self):
        return sum([item.price for item in self.orderitem_set.all()])


pre_save.connect(check_phone, sender=Order)


class OrderItem(models.Model):
    user_form = models.ForeignKey(Order, on_delete=models.CASCADE)
    item = models.ForeignKey(Pizza, on_delete=models.DO_NOTHING)
    size = models.CharField(max_length=100, choices=Size.CHOICES)
    quantity = models.PositiveSmallIntegerField()

    def __str__(self):
        return f"Item"

    @property
    def price(self):
        return self.item.sizes.get(type=self.size).price * self.quantity
