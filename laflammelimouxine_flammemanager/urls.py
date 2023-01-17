"""laflammelimouxine_flammemanager URL Configuration

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
from flammemanager import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('add_client/', views.add_client, name='add_client'),
    path('save_client/', views.save_client, name='save_client'),
    path('list_client/', views.list_client, name='list_client'),
    path('add_produit/', views.add_produit, name='add_produit'),
    path('list_produit/', views.list_produit, name='list_produit'),
]
