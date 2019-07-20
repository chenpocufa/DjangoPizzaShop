from django.contrib import admin
from .models import Category, Pizza, Size


class SizeInline(admin.TabularInline):
    model = Size
    extra = 0
    max_num = 2


class PizzaAdmin(admin.ModelAdmin):
    list_display = ('name',)
    fields = ('name', 'description', 'category', 'photo')
    list_filter = ('category__name',)
    inlines = (SizeInline,)


admin.site.register(Category)
admin.site.register(Pizza, PizzaAdmin)
