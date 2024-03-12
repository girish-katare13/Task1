from django.contrib import admin
from .models import CustomUser

# Register your models here.
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email', 'user_type')  # Customize which fields to display in the admin list view

admin.site.register(CustomUser, CustomUserAdmin)