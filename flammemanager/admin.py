from django.contrib import admin
from django.contrib.admin import AdminSite
from django.contrib.auth.models import User, Group
from django.contrib.auth.admin import UserAdmin
from .models import Commande, Client, Produit, Livraison

admin_site = AdminSite(name='Mon Administration')
admin_site.site_header = 'Flamme Manager'
admin_site.site_title = 'Flamme Manager'
admin_site.index_title = 'Bienvenue dans Flamme Manager'

admin_site.register(Commande)
admin_site.register(Client)
admin_site.register(Produit)
admin_site.register(Livraison)
#admin_site.register(User)
#admin_site.register(Group)


# Register your models here.

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    list_filter = ('is_staff', 'is_superuser', 'is_active')
    search_fields = ('username', 'first_name', 'last_name', 'email')
    ordering = ('username',)
    filter_horizontal = ('groups', 'user_permissions')

