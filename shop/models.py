from django.db import models


class Order(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}, {self.phone}"


class OrderItem(models.Model):
    user_form = models.CharField(max_length=100)
    item_name = models.CharField(max_length=100)
    item_price = models.CharField(max_length=100)
    size = models.CharField(max_length=100)
    quantity = models.CharField(max_length=100)

    def __str__(self):
        return f"name = {self.item_name}, price = {self.item_price}, size = {self.size}, quantity = {self.quantity}" \
            f", order = {self.user_form}"
