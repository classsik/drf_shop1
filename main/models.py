from django.db import models
from django.contrib.auth.models import User


class Manufacturer(models.Model):
    title = models.CharField(max_length=100)


class Country(models.Model):
    title = models.CharField(max_length=100)


class Product(models.Model):
    title = models.CharField(max_length=100)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    new = models.BooleanField()
    price = models.IntegerField()


class Cart(models.Model):
    products = models.ManyToManyField(Product)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Order(models.Model):
    total_price = models.IntegerField(null=True, blank=True)
    products = models.ManyToManyField(Product)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
