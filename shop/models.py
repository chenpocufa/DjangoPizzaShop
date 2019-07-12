from django.db import models


class Order(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)

    def __str__(self):
        return self.name, self.phone
