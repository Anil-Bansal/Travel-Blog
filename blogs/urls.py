from django.urls import path

from . import views

urlpatterns=[
    path('home',views.home,name="home"),
    path('profile',views.profile,name="profile"),
    path('addblogs',views.addblogs,name="addblogs"),
    path('like_blog',views.likeblog,name="like_blog"),
    path('favourite',views.favourite,name="favourite"),
    ]