from django.shortcuts import get_object_or_404, redirect, render
from .models import Blog
# Create your views here.
def home(request):
    if request.method=='POST':
        username=request.session['user']
        user=request.POST['search']
        blogs=Blog.objects.filter(username=user)
        blogs=blogs[::-1]
        return render(request, 'home.html', {
            'blogs': blogs,
            'user': username
        })
    else:
        if 'user' not in request.session:
            return redirect('/')
        username=request.session['user']
        blogs = Blog.objects.all().exclude(username=username)
        blogs=blogs[::-1]
        return render(request, 'home.html', {
            'blogs': blogs,
            'user': username
        })

def profile(request):
    if 'user' not in request.session:
        return redirect('/')
    username=request.session['user']
    blogs=Blog.objects.filter(username=username)
    blogs=blogs[::-1]
    return render(request, 'profile.html', {
        'blogs': blogs,
        'user': username
    })

def addblogs(request):
    if 'user' not in request.session:
        return redirect('/')
    username=request.session['user']
    if request.method=='POST':
        title=request.POST['title']
        description=request.POST['description']
        blog=Blog(username=username,title=title,description=description)
        blog.save()
        return redirect('/blogs/profile')
    else:
        return render(request,'addblog.html',{
            'user': username
        })
    