from __future__ import unicode_literals
from django.db import models
from csc341_final.settings import BASE_DIR, MEDIA_URL
import os 

# Create your models here.
class Cookie(models.Model):
    cookieid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    price = models.FloatField()
    peanuts = models.BooleanField(default=False)
    description = models.CharField(max_length = 100)
    imagePath = models.ImageField(default = os.path.join(BASE_DIR, MEDIA_URL, 'notAvailable.jpg'))
    
    def __str__(self):
        return(self.name)
        
        
class Customer(models.Model):
    custid = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    
    def __str__(self):
        return('{} {}'.format(self.firstname, self.lastname))
        
class Address(models.Model):
    custid = models.IntegerField(primary_key=True)
    streetone = models.CharField(max_length=50, null = True)
    streettwo = models.CharField(max_length=50, null = True)
    city = models.CharField(max_length=20, null = True)
    state = models.CharField(max_length=20, null = True)
    zipcode = models.CharField(max_length=5, null = True)
    country = models.CharField(max_length=25, null = True)
    
class Orders(models.Model):
    orderid = models.AutoField(primary_key=True)
    custid = models.ForeignKey(Customer, on_delete=models.CASCADE)
    cookieid = models.ForeignKey(Cookie)
    cookamt = models.IntegerField()
    price = models.FloatField()
    
class ShoppingCart(models.Model):
    custid = models.ForeignKey(Customer, on_delete=models.CASCADE)
    cookieid = models.ForeignKey(Cookie)
    quantity = models.IntegerField()