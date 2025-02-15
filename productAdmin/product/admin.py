from django.contrib import admin
from .models import Product,Profile  # Import your Product model

# Register your model
admin.site.register(Product)
admin.site.register(Profile)

