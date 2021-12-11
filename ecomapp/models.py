from django.db import models
from django.db.models.base import Model

# Create your models here.
class Products(models.Model):
    def __str__(self):
        return self.title
    title = models.CharField(max_length=300)
    price = models.FloatField()
    discount_price = models.FloatField()
    category = models.CharField(max_length=200)
    description = models.TextField()
    image = models.CharField(max_length=500)
    

class Order(models.Model):
    items=models.CharField(max_length=1000)
    name=models.CharField(max_length=300)
    email=models.CharField(max_length=300)
    address=models.CharField(max_length=1000)
    city=models.CharField(max_length=300)
    state=models.CharField(max_length=300)
    zipcode=models.CharField(max_length=300)
    total=models.CharField(max_length=20)