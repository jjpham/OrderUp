from django.db import models
from django.urls import reverse
from datetime import date

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
    address = models.ForeignKey(Address, on_delte=models.CASCADE)

    def __str__(self):
        return self.name
class Order(models.Model):
    cost = models.IntegerField()
    address = models.ForeignKey(Address, on_delte=models.CASCADE)
    phone_number = models