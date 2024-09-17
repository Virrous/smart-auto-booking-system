from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password

def index(request):
    return render(request, 'index.html')

def driver_form(request):
     if request.method == 'POST':
        if 'login' in request.POST:
            # Handle Login
            email = request.POST.get('email')
            password = request.POST.get('password')
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                messages.error(request, 'Invalid email or password')
        elif 'register' in request.POST:
            # Handle Registration
            fname = request.POST.get('fname')
            lname = request.POST.get('lname')
            phone = request.POST.get('phone')
            email = request.POST.get('email')
            password = request.POST.get('password1')
            confirm_password = request.POST.get('password2')
            city = request.POST.get('city')
            lisense_num = request.POST.get('lisense-num')

            # Validate Password
            if password != confirm_password:
                messages.error(request, 'Passwords do not match')
            else:
                # Check if the email is already registered
                if Customer.objects.filter(email=email).exists():
                    messages.error(request, 'Email is already registered')
                else:
                    # print(fname,lname,phone,email,password,city,lisense_num)
                    # Hash the password before saving
                    hashed_password = make_password(password)
                    driver = Driver(fname=fname, lname=lname, phone=phone, email=email, password=hashed_password, city=city, lisense_num = lisense_num)
                    # print(driver)
                    try:
                        driver.save()
                        messages.success(request, 'Registration successful! You can now log in.')
                    except Exception as e:
                        messages.error(request, f'Error saving to database: {str(e)}')
                    messages.success(request, 'Registration successful! You can now log in.')
                    return redirect('index')

     return render(request, 'driver_form.html')
 
def driver_dash(request):
     return render(request, 'rider-dashboard.html')

def customer_form(request):
    if request.method == 'POST':
        if 'login' in request.POST:
            # Handle Login
            email = request.POST.get('email')
            password = request.POST.get('password')
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                messages.error(request, 'Invalid email or password')
        elif 'Register' in request.POST:
            # Handle Registration
            first_name = request.POST.get('fname')
            last_name = request.POST.get('lname')
            phone = request.POST.get('phone')
            email = request.POST.get('reg-email')
            password = request.POST.get('reg-password')
            confirm_password = request.POST.get('confirm-password')
            city = request.POST.get('city')

            # Validate Password
            if password != confirm_password:
                messages.error(request, 'Passwords do not match')
            else:
                # Check if the email is already registered
                if Customer.objects.filter(email=email).exists():
                    messages.error(request, 'Email is already registered')
                else:
                    # Hash the password before saving
                    hashed_password = make_password(password)
                    user = Customer(first_name=first_name, last_name=last_name, phone=phone, email=email, password=hashed_password, city=city)
                    user.save()
                    messages.success(request, 'Registration successful! You can now log in.')
                    return redirect('index')

    return render(request, 'customer_form.html')

def customer_dash(request):
    return render(request, 'customer-dash.html')