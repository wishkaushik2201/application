from unicodedata import category
from django.contrib import admin
from .models import login_user, upload_image,product,category,order
# Register your models here.

admin.site.register(login_user)
admin.site.register(upload_image)
admin.site.register(product)
admin.site.register(category)
admin.site.register(order)