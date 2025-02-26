from django.contrib.auth.models import User
from django.db import models
import django_filters


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(default="update product")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    expire_date = models.DateField(null=True, blank=True)  # Allows manual input
    stock = models.IntegerField(default=1)
    image = models.ImageField(upload_to='product_images/', blank=True, null=True)

    def __str__(self):
        return self.name





