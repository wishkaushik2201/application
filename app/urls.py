from unicodedata import name
# from xml.etree.ElementInclude import include
from django import views
from django.contrib import admin
from django.db import router
from django.urls import path,include
from . import views
from app.views import demo_REST
from rest_framework import routers,serializers,viewsets

router=routers.DefaultRouter()
router.register(r"user",demo_REST, basename="MyModel")
3

urlpatterns = [
    path('',views.home, name='home'),
    path('contact/',views.contact, name='contact'),
    path('login_in',views.log, name= 'login_in'),
    path('sign_in',views.sign_in, name= 'sign_in'),
    path('logout',views.logout, name='logout'),
    path('cart/',views.cart, name='cart'),
    path('checkout',views.checkout, name='checkout'),
    path("order/",views.order_dtls, name="order"),
    path('',include(router.urls)),
    path('api_auth/',include('rest_framework.urls', namespace='rest_framework'))
]