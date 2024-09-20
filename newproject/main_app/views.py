from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password,check_password

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'Aboutus.html')

def driver_form(request):
     if request.method == 'POST':
        if 'login' in request.POST:
            # Handle Login
            auto_number = request.POST.get('auto-num')
            password = request.POST.get('password')
            credidentals = Driver.objects.all()
            for credential in credidentals:
                if credential.auto_number == auto_number and credential.password == password:
                    return redirect('driver_dash')
                else:
                    
                    return redirect('driver_form')
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
            auto_number = request.POST.get('auto-num')

            # Validate Password
            if password != confirm_password:
                messages.error(request, 'Passwords do not match')
            else:
                driver = Driver(fname=fname, lname=lname, phone=phone, email=email, password=password,city=city, lisense_num = lisense_num, auto_number = auto_number)
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
            credidentals = Customer.objects.all()
            for customer in credidentals:
                if customer.email == email and customer.password == password:
                    return redirect('mapping')
                else:
                    return redirect('customer_form')
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
                user = Customer(first_name=first_name, last_name=last_name, phone=phone, email=email,password=password, city=city)
                user.save()
                messages.success(request, 'Registration successful! You can now log in.')
                return redirect('index')

    return render(request, 'customer_form.html')

def mapping(request):
    return render(request, 'mapping.html')

def customer_dash(request):
    return render(request, 'customer-dash.html')

def customer_profile(request):
    return render(request, 'profile.html')
