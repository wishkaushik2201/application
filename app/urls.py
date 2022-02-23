from unicodedata import name
from django import views
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('contact/',views.contact, name='contact'),
    path('login_in',views.log, name= 'login_in'),
    path('sign_in',views.sign_in, name= 'sign_in'),
    path('logout',views.logout, name='logout'),
    path('cart/',views.cart, name='cart'),
    path('checkout',views.checkout, name='checkout'),
    path("order/",views.order_dtls, name="order")
]



