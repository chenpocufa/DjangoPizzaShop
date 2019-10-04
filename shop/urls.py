from django.urls import path, include
from . import views
from accounts import views as acc_views
from rest_framework import routers


router = routers.DefaultRouter()
router.register('users/', acc_views.UserViewSet)
app_name = 'shop'


urlpatterns = [
    path('', views.home, name='shop-home'),
    path('api', include(router.urls)),
    path('about/', views.about, name='shop-about'),
    path('cart/', views.cart, name='shop-cart'),
    path('order/', views.order, name='shop-order'),
    path('register/', views.register, name='shop-register'),
    path('profile/', views.profile, name='shop-profile'),
    path('timetable/', views.timetable, name='shop-timetable'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
