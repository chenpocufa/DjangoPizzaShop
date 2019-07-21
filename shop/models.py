from django.db import models
from catalog.models import Pizza


class Order(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}, {self.phone}"


class OrderItem(models.Model):
    user_form = models.ForeignKey(Order, on_delete=models.CASCADE)
    item = models.ForeignKey(Pizza, on_delete=models.DO_NOTHING)
    size = models.CharField(max_length=100)
    quantity = models.CharField(max_length=100)

    def __str__(self):
        return f"Item"
