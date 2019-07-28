from django.db import models
from catalog.models import Pizza, Size


class Order(models.Model):
    phone = models.CharField(max_length=100)
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.phone}, {self.name}"

    @property
    def total_price(self):
        return sum([item.price for item in self.orderitem_set.all()])


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
