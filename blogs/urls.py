from django.urls import path

from . import views

urlpatterns=[
    path('home/<username>/',views.home,name="home"),
    path('profile/<username>/',views.profile,name="profile"),
    path('addblogs/<username>/',views.addblogs,name="addblogs")
    ]