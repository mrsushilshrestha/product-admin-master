from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(default="update product")
    category = models.CharField(max_length=100)
    expire_date = models.DateField(auto_now_add=True)
    stock = models.IntegerField(default=1)
    image = models.ImageField(upload_to='product_images/', blank=True, null=True)

    def __str__(self):
        return self.name



class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

