from django.shortcuts import get_object_or_404, redirect, render
from .models import Blog,LikedBlog
import json
# Create your views here.
def home(request):
    if request.method=='POST':
        username=request.session['user']
        user=request.POST['search']
        blogs=Blog.objects.filter(username=user)
        blogs=blogs[::-1]
        obj=LikedBlog.objects.filter(username=username)
        jsonDec = json.decoder.JSONDecoder()
        likedlist = jsonDec.decode(obj[0].likedlist)
        num_list=[int(x) for x in likedlist]
        return render(request, 'home.html', {
            'blogs': blogs,
            'user': username,
            'likedlist':num_list
        })
    else:
        if 'user' not in request.session:
            return redirect('/')
        username=request.session['user']
        blogs = Blog.objects.all().exclude(username=username)
        blogs=blogs[::-1]
        obj=LikedBlog.objects.filter(username=username)
        jsonDec = json.decoder.JSONDecoder()
        likedlist = jsonDec.decode(obj[0].likedlist)
        num_list=[int(x) for x in likedlist]
        return render(request, 'home.html', {
            'blogs': blogs,
            'user': username,
            'likedlist':num_list
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
        image=request.POST['image']
        blog=Blog(username=username,title=title,description=description,image=image)
        blog.save()
        return redirect('/blogs/profile')
    else:
        return render(request,'addblog.html',{
            'user': username
        })

def likeblog(request):
    id=request.POST['blog_id']
    username=request.session['user']
    blogs = Blog.objects.all().exclude(username=username)
    blogs=blogs[::-1]
    obj=LikedBlog.objects.filter(username=username)
    jsonDec = json.decoder.JSONDecoder()
    likedlist = jsonDec.decode(obj[0].likedlist)
    if id in likedlist:
        likedlist.remove(id)
    else:
        likedlist.append(id)

    LikedBlog.objects.filter(username=username).update(likedlist=json.dumps(likedlist))
    num_list=[int(x) for x in likedlist]
    return render(request, 'home.html', {
        'blogs': blogs,
        'user': username,
        'likedlist': num_list
    })
    