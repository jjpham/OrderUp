from django.db import models
from django.urls import reverse
from datetime import date

from main_app.fields import PhoneNumberField, CostField

from django.contrib.auth.models import User
# Create your models here.


class Restaurant(models.Model):
    name = models.CharField(max_length = 100)
    food_type = models.CharField(max_length=50)
    address = models.TextField(max_length=300)
    phone_number = PhoneNumberField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('detail',kwargs={'restaurant_id':self.id})
    
class Menu_Item(models.Model):
    name = models.CharField(max_length = 100)
    price = CostField(max_digits=10, decimal_places=2)
    description = models.TextField(max_length =250)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('detail',kwargs={'restaurant_id':self.restaurant.id})

class Order(models.Model):
    name = models.CharField(max_length=100, default='Meal')
    cost = models.IntegerField()
    address = models.TextField(max_length=300)
    phone_number = PhoneNumberField()
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    menu_item = models.ManyToManyField(Menu_Item)
    def get_total_cost(self):
        total_cost = 0
        for item in self.menu_items.all():
            total_cost =+ item.price
        return total_cost
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('detail',kwargs={'restaurant_id':self.restaurant.id})
