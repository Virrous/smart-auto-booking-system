from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def customer_form(request):
    return render(request,'customer_form.html')

def driver_form(request):
    return render(request,'driver_form.html')