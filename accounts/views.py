from django.shortcuts import render, redirect
from .models import User

# Create your views here.


def register(request):
    if request.method=='POST':
        print("I'm here")
        username=request.POST['username']
        password=request.POST['password1']
        user=User(username=username, password=password)
        user.save()
        return redirect('/home')
    else:
        return render(request,'register.html')

def login(request):
    return render(request,'login.html')

def home(request):
    return render(request,'home.html') 
