from django.shortcuts import get_object_or_404, redirect, render
from .models import Blog
# Create your views here.
def home(request, username):
    blogs = Blog.objects.all()
    print(len(blogs))
    return render(request, 'home.html', {
        'blogs': blogs
    })