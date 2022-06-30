from django.contrib import admin
from .models import Post
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at', 'published']  # здесь указываются поля, которые вы хотите видеть в админке для этой модели
    list_filter = ['created_at', 'published']  # здесь указываются фильтры в админке для этой модели


admin.site.register(Post, PostAdmin)
