from django.contrib import admin
from .models import Post, Author, Book


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'user', 'created']


@admin.register(Author)
class PostAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'date_of_birth', 'date_of_death']


@admin.register(Book)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'summary', 'price', 'amount']
