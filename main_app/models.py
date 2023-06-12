from django.db import models
from django.urls import reverse
from datetime import date

from main_app.fields import PhoneNumberField, CostField

from django.contrib.auth.models import User
# Create your models here.

class Address(models.Model):
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.street},{self.city},{self.state},{self.zip_code}'


class Restaurant(models.Model):
    name = models.CharField(max_length = 100)
    food_type = models.CharField(max_length=50)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class Menu_Item(models.Model):
    name = models.CharField(max_length = 100)
    price = CostField(max_digits=10, decimal_places=2)
    description = models.TextField(max_length =250)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

class Order(models.Model):
    cost = models.IntegerField()
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    phone_number = PhoneNumberField()
    menu_items = models.ManyToManyField(Menu_Item)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    def get_total_cost(self):
        total_cost = 0
        for item in self.menu_items.all():
            total_cost =+ item.price
        return total_cost