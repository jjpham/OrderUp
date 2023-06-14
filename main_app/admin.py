from django.contrib import admin
from .models import Restaurant, Order, Menu_Item
# Register your models here.
admin.site.register(Restaurant)
admin.site.register(Order)
admin.site.register(Menu_Item)
