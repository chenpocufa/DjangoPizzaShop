"""
Catalogue models.
"""
from django.db import models
from django.forms.models import model_to_dict


class Category(models.Model):
    """
    Category model.
    """
    name = models.CharField(
        max_length=100,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'


class Pizza(models.Model):
    """
    Pizza model.
    """
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    category = models.ManyToManyField(Category)
    photo = models.ImageField(upload_to='images/')

    @property
    def categories_display(self):
        return ' '.join(str(cat) for cat in self.category.all())

    def __str__(self):
        #    return "name = {}, size = {}".format(self.name, self.size)
        #    return "name = %s, size = %s" % (self.name, self.size)
        return f"{self.name} pizza"

    def order(self, fields=None):
        _fields = ['name'] if fields is None else fields
        return model_to_dict(self, fields=_fields)

    # @property
    # def sizes(self):
    #     return self.size_set.all()


class Size(models.Model):
    type = models.CharField(max_length=20)
    price = models.FloatField(default=0)
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE, related_name='sizes')
    active = models.BooleanField(default=False)

    def __str__(self):
        return f"Size {self.id}"
