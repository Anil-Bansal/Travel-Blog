from django.shortcuts import get_object_or_404, redirect, render
from .models import Blog
# Create your views here.
def home(request,username):
    print(request)
    username=username[9:]
    blogs = Blog.objects.all().exclude(username=username)
    return render(request, 'home.html', {
        'blogs': blogs,
        'user': username
    })

def profile(request,username):
    username=username[9:]
    blogs=Blog.objects.filter(username=username)
    return render(request, 'profile.html', {
        'blogs': blogs,
        'user': username
    })

def addblogs(request,username):
    username=username[9:]
    if request.method=='POST':
        title=request.POST['title']
        description=request.POST['description']
        blog=Blog(username=username,title=title,description=description)
        blog.save()
        url="/blogs/profile/username="+username
        return redirect(url)
    else:
        return render(request,'addblog.html',{
            'user': username
        })
    