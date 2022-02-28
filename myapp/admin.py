from django.contrib import admin

# Register your models here.
from .models import LoginTotalUsers, Post

# admin.site.register(Post)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Post._meta.get_fields()]


@admin.register(LoginTotalUsers)
class LoginTotalUsersAdmin(admin.ModelAdmin):
    list_display = [field.name for field in LoginTotalUsers._meta.get_fields()]
