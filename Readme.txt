female_obj = Category.objects.filter(category="female").first()
female_obj.__dict__

-----------------
product.objects.filter.(category__id="2").count()