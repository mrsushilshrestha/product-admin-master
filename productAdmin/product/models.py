from django.contrib.auth.models import User
from django.db import models
import django_filters

#model for category
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

#model for Product
class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(default="update product")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    expire_date = models.DateField(null=True, blank=True)  # Allows manual input
    stock = models.IntegerField(default=1)
    image = models.ImageField(upload_to='product_images/', blank=True, null=True)

    def __str__(self):
        return self.name


#For Profile
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15, blank=True, null=True)
    avatar = models.ImageField(upload_to='avatars/', default='avatars/default.png')

    def __str__(self):
        return self.user.username
