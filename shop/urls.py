from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='shop-home'),
    path('about/', views.about, name='shop-about'),
    path('cart/', views.cart, name='shop-cart'),
    path('order/', views.order, name='shop-order'),
]
