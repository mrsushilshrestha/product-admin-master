from django.contrib.auth.models import User
from django.db import models
<<<<<<< HEAD
import django_filters


class Category(models.Model):
    name = models.CharField(max_length=100)
=======


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)  # Unique constraint to prevent duplicate categories

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(default="update product")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")  # Normalized category
    expire_date = models.DateField(auto_now_add=True)
    stock = models.PositiveIntegerField(default=1)  # Prevent negative stock values
    image = models.ImageField(upload_to='product_images/', blank=True, null=True)

>>>>>>> fd80f66bc3a6993191e1fdfa55994465fa96aee3

    def __str__(self):
        return self.name

<<<<<<< HEAD
class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(default="update product")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    expire_date = models.DateField(null=True, blank=True)  # Allows manual input
    stock = models.IntegerField(default=1)
    image = models.ImageField(upload_to='product_images/', blank=True, null=True)

    def __str__(self):
        return self.name





=======

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15, blank=True, null=True)
    avatar = models.ImageField(upload_to='avatars/', default='avatars/default.png')

    def __str__(self):
        return self.user.username
>>>>>>> fd80f66bc3a6993191e1fdfa55994465fa96aee3
