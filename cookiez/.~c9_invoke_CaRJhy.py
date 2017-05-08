from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Cookie(models.Model):
    cooki
    name = models.CharField(max_length=20)
    price = models.FloatField()
    peanuts = models.BooleanField(default=False)
    
class Customer(models.Model):
    custid = models.IntegerField(primary_key=True)
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    
class Address(models.Model):
    custid = models.IntegerField(primary_key=True)
    streetone = models.CharField(max_length=50)
    streettwo = models.CharField(max_length=50)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    zipcode = models.CharField(max_length=5)
    country = models.CharField(max_length=25)
    
class Orders(models.Model):
    orderid = models.IntegerField(primary_key=True)
    custid = models.ForeignKey(Customer, on_delete=models.CASCADE)
    cookieid = models.ForeignKey(Cookie)
    cookamt = models.IntegerField()
    price = models.FloatField()