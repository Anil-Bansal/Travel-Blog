from django.shortcuts import render, redirect
from .models import User
from blogs.models import LikedBlog
from django.contrib import messages
import json

# Create your views here.


def register(request):
    if 'user' in request.session:
        return redirect('blogs/home')
    if request.method=='POST':
        username=request.POST['username']
        password1=request.POST['password1']
        password2=request.POST['password2']
        if password1==password2:
            user_same=User.objects.filter(username=username)
            if len(user_same)>0:
                messages.info(request,"Username exists")
                return redirect('/')
            else:
                user=User(username=username, password=password1)
                user.save()
                obj=LikedBlog(username=username)
                cur_list=[]
                obj.likedlist=json.dumps(cur_list)
                obj.save()
                request.session['user']=username
                return redirect('blogs/home')
        else:
            messages.info(request,"Password MisMatch")
            return redirect('/')
    else:
        return render(request,'register.html')

def login(request):
    if 'user' in request.session:
        return redirect('blogs/home')
    if request.method=='POST':
        username=request.POST['username']
        password1=request.POST['password1']
        get_users=User.objects.filter(username=username,password=password1)
        if len(get_users)>0:
            request.session['user']=username
            return redirect('blogs/home')
        else:
            messages.info(request,"User Does Not Exist")
            return redirect('/login')
    else:
        return render(request,'login.html')

def signout(request):
    del request.session['user']
    return redirect('/')
