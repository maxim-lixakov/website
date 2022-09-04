from django.contrib import admin
from .models import User, User_data


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('login', 'reg_date', 'name')
@admin.register(User_data)
class UserDataAdmin(admin.ModelAdmin):
    list_display = ('year', 'month', 'day', 'text', 'login')