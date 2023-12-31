from django.contrib import admin
from .models import Comment, Post, Category

# Register your models here.

admin.site.register(Category)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'created', 'publish', 'author')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'body')
    ordering = ('author', 'status', 'publish')
    list_filter = ('author', 'created', 'publish')


@admin.register(Comment)
class Comments(admin.ModelAdmin):
    list_display = ['username', 'email', 'created']