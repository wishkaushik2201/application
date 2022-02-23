from statistics import mode
from telnetlib import STATUS
from unicodedata import name
from urllib import request
from click import password_option
from django.db import models
from numpy import imag
from tables import Description
import datetime

# Create your models here.
class login_user(models.Model):
    username = models.CharField(max_length=50)
    passw= models.CharField(max_length=255)

class upload_image(models.Model):
    name=models.CharField(max_length=50)
    image=models.ImageField(upload_to="upload/product")

    def __str__(self):
        return self.name

#register table
# class reg(models.Model):
#     fname=models.CharField(max_length=20)
#     lname=models.CharField(max_length=20)
#     gender=models.CharField(max_length=10)
#     email=models.EmailField(max_length=254)
#     password1=models.CharField(max_length=255)
#     DateofBirth=models.CharField(max_length=20)
#     mobileno=models.CharField(max_length=20)

#     def __str__(self):
#         return self.fname
class category(models.Model):
    name=models.CharField(max_length=50)
    def __str__(self):
        return self.name

class product(models.Model):
    name=models.CharField(max_length=50)
    image=models.ImageField(upload_to='upload/product')
    price=models.IntegerField(default=100)
    description=models.CharField(max_length=255, default="good")
    category=models.ForeignKey(category,on_delete=models.CASCADE,default=1)
    
    def __str__(self):
        return self.name

class order(models.Model):
    product=models.ForeignKey(product,on_delete=models.CASCADE)
    customer=models.ForeignKey(login_user,on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1)
    price=models.IntegerField()
    address=models.CharField(max_length=50,default="", blank=True)
    phone=models.IntegerField(default=1)
    date=models.DateField(default=datetime.datetime.today)
    status=models.BooleanField(default=False)
    def __str__(self):
        return self.address