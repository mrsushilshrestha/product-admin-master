from django.shortcuts import render,get_object_or_404, redirect
from django.http.response import HttpResponse

from django.contrib.auth import login as auth_login ,logout as auth_logout
from django.contrib.auth.models import User
from django.contrib.auth. hashers import make_password,check_password
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

from .models import Product,Category
from django.shortcuts import render, redirect

#delete product
def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    product.delete()
    return redirect('products')  # Redirect to the product list page

#product
@login_required(login_url='/login') #make loging required
def products(request):
    products = Product.objects.all()    
    return render(request, 'products.html', {'products': products, 'active_page': 'products'})


#add new Product
@login_required(login_url='/login/')
def add_products(request):
    if request.method == "POST":
        name = request.POST.get('name')
        description = request.POST.get('description')
        category_id = request.POST.get('category')
        expire_date = request.POST.get('expire_date')
        stock = request.POST.get('stock')
        image = request.FILES.get('image')  

        category = Category.objects.get(id=category_id)  # Get category object

        product = Product(
            name=name,
            description=description,
            category=category,
            expire_date=expire_date,
            stock=stock,
            image=image  
        )
        product.save()

        return redirect('products')  # Redirect to products page

    categories = Category.objects.all()
    return render(request, "add-product.html", {"categories": categories})


#add category
def add_category(request):
    if request.method == "POST":
        category_name = request.POST.get('category_name')

        # Save the new category to the database
        Category.objects.create(name=category_name)
        
        return redirect('products')  # Redirect after category creation
    return render(request, "add-category.html")


#edit product
@login_required(login_url='/login')
def edit_products(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        # Handle form submission and update product
        product.name = request.POST['name']
        product.description = request.POST['description']
        product.category_id = request.POST['category']
        product.expire_date = request.POST['expire_date']
        product.stock = request.POST['stock']

        if 'image' in request.FILES:
            product.image = request.FILES['image']

        product.save()
        return redirect('products')  # Redirect to products list or success page

    return render(request, 'edit-product.html', {'product': product})

#index page
@login_required(login_url='/login')
def index(request):
    
    return render(request,'index.html',{'active_page': 'dashboard'})

#logout the user
def custom_logout(request):
    auth_logout(request)
    return redirect('login')  # Redirect to login page after logout


#account
@login_required(login_url='/login')
def customer_account(request):    
    return render(request,'accounts.html',{'active_page': 'account'})

#setting
@login_required(login_url='/login')
def customer_setting(request):    
    return render(request,'edit-product.html',{'active_page': 'setting'})


@login_required
def update_profile(request):
    profile = request.user.profile

    if request.method == 'POST':
        # Handle avatar and phone update
        if 'avatar' in request.FILES:
            profile.avatar = request.FILES['avatar']
        profile.phone = request.POST.get('phone')
        profile.save()

        # Update user info (username, email)
        request.user.username = request.POST.get('name')
        request.user.email = request.POST.get('email')
        request.user.set_password(request.POST.get('password'))  # Optional: Password change
        request.user.save()

        return redirect('profile')  # Redirect to the profile page after updating

    return render(request, 'update_profile.html', {'user': request.user})

#signup user
def signup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        password=make_password(password)
        first_name = request.POST.get('first_name')        
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        
        User.objects.create(username=username,password=password,first_name=first_name,last_name=last_name,email=email)
        
    return render(request,"signup-user.html")

# def login(request):
#     payload = request.POST
#     if payload:
#         username =payload['username']
#         password = payload['password']
#         print("username: ",username, "password: ",password)
#         user_obj =Account.objects.filter(username=username)
#         if user_obj.exists():
#             user_obj =user_obj.first()
            
#             check_password_data = check_password(password,user_obj.password)
#             print(check_password_data)
#             if(check_password_data):
#                 login(request,user_obj)
#                 return HttpResponse(f"congratulation you are login!!{check_password_data}")
#             else:
#                 return HttpResponse(f"congratulation you are login!!{check_password_data}")
#     return render(request,"login-user.html")


def login_user(request):
    if request.method == "POST":
        payload =request.POST
        username = request.POST.get('username')
        password = request.POST.get('password')
        next= payload.get('next')

        print("Username:", username, "Password:", password)

        # Fetch the first user with the matching username (avoiding MultipleObjectsReturned error)
        user_obj = User.objects.filter(username=username).first()  
        print(user_obj)
    
        if not user_obj:  # If no user found
            return HttpResponse("Invalid username or password")
        # authenticate(username="john", password="secret")
        check_password_data = check_password(password, user_obj.password)
        print(password)
        print(user_obj.password)
        if check_password_data:
            auth_login(request,user_obj)
            if next:
                return redirect(next)
            return redirect('index')  
        else:
            return HttpResponse("Invalid username or password")
        
    return render(request,"login.html",{'next':request.GET.get('next')})


