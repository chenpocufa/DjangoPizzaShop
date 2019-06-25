"""
Catalogue models.
"""
from django.db import models


class Size(models.Model):
    SMALL = 'Small'
    LARGE = 'Large'
    SIZE = [
        (SMALL, 'Small'),
        (LARGE, 'Large')
    ]

    size = models.CharField(
        max_length=5,
        choices=SIZE,
        default=LARGE
    )

    def __str__(self):
        return self.size


class Category(models.Model):
    """
    Category model.
    """
    CLASSIC = 'classic'
    VEGETARIAN = 'vegetarian'
    SPICY = 'spicy'
    TYPE = [
        (CLASSIC, 'classic'),
        (VEGETARIAN, 'vegetarian'),
        (SPICY, 'spicy')
    ]

    type = models.CharField(
        max_length=100,
        choices=TYPE
    )

    def __str__(self):
        return self.type

    class Meta:
        verbose_name_plural = 'Categories'


class Pizza(models.Model):
    """
    Pizza model.
    """
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    price_small = models.IntegerField()
    price_large = models.IntegerField()
    category = models.ManyToManyField(Category)
    photo = models.ImageField(upload_to='images/')

    @property
    def categories_display(self):
        return ' '.join(str(cat) for cat in self.category.all())

    def __str__(self):
        #    return "name = {}, size = {}".format(self.name, self.size)
        #    return "name = %s, size = %s" % (self.name, self.size)
        return f"name = {self.name}, prices = {self.price_small}, {self.price_large}, category = {', '.join(str(cat) for cat in self.category.all())}"
