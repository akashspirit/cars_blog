"""blogproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from blogapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.show,name="show"),
    path('add',views.add1,name="add1"),
    path('MoreInfo <int:id>',views.MoreInfo, name="MoreInfo"),
    path('r',views.register,name='register'),
    path('login',views.login, name="login"),
    path('logout',views.logout,name='logout'),
    path('search',views.search,name='search'),
    path('delete<int:id>',views.delete,name="delete"),
    path('edit<int:id>',views.edit,name="edit"),
    path('profile',views.profile_a,name="profile"),
    path('feedback',views.feedback1,name='feedback'),




]
