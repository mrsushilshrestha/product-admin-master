from django.shortcuts import render
from django.http.response import HttpResponse

from django.contrib.auth import login as auth_login ,logout as auth_logout
from django.contrib.auth.models import User
from django.contrib.auth. hashers import make_password,check_password
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
# def login(request):
    
#     return render(request,'login.html')

@login_required(login_url='/login')
def products(request):    
    return render(request,'products.html',{'active_page': 'products'})

@login_required(login_url='/login/')
def add_products(request):
    
    return render(request,'add-product.html')

@login_required(login_url='/login')
def edit_products(request):
    
    return render(request,'edit-product.html')

@login_required(login_url='/login')
def index(request):
    
    return render(request,'index.html',{'active_page': 'dashboard'})

#logout the user
def custom_logout(request):
    auth_logout(request)
    return redirect('login')  # Redirect to login page after logout

def customer_account(request):
    
    return HttpResponse("This is Account Pages",{'active_page': 'account'})

def customer_setting(request):
    
    return HttpResponse('hello from setting',{'active_page': 'setting'})


# Create your views here.
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