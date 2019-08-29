from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='shop-home'),
    path('about/', views.about, name='shop-about'),
    path('cart/', views.cart, name='shop-cart'),
    path('order/', views.order, name='shop-order'),
    path('register/', views.register, name='shop-register'),
    path('profile/', views.profile, name='shop-profile'),
    path('timetable/', views.timetable, name='shop-timetable'),
    path('accounts/', include('django.contrib.auth.urls')),
]
