from django.contrib import admin
from .models import Category, Pizza


class PizzaAdmin(admin.ModelAdmin):
    list_display = ('name', 'price_small', 'price_large')
    fields = ('name', 'description', 'price_small', 'price_large', 'category', 'photo')
    list_filter = ('category__name',)


admin.site.register(Category)
admin.site.register(Pizza, PizzaAdmin)
