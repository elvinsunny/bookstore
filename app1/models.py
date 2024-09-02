
from django.db import models
import datetime

from django.contrib.auth.models import User


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField(null=False)
    description = models.CharField(max_length=500)
    image = models.ImageField(upload_to='static/')
    isbn = models.CharField(max_length=13, null=True, blank=True)
    binding = models.CharField(max_length=50, null=True, blank=True)
    language = models.CharField(max_length=50, null=True, blank=True)
    publishing_date = models.DateField(null=True, blank=True)
    edition = models.PositiveIntegerField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.PositiveIntegerField(default=1)


    def __str__(self):
        return self.name
    
class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)  # Add default value here
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
 
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(CartItem)
    total_quantity = models.PositiveIntegerField()
    total_price = models.FloatField()
    billing_address = models.TextField()
    created_at = models.DateTimeField(default=datetime.datetime.now)

    
    # Add other fields as needed for billing information (e.g., name, address, etc.)
    # ...

    def __str__(self):
        return f"Order #{self.pk} - {self.user.username}"

