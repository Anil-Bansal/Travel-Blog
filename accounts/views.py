from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth

# Create your views here.

def register(request):
    if request.method=='POST':
        print("I'm here")
        username=request.POST['username']
        password=request.POST['password1']
        
        return redirect('/home')
    else:
        return render(request,'register.html')

def login(request):
    return render(request,'login.html')

def home(request):
    return render(request,'home.html')