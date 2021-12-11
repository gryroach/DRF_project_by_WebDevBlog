from django.contrib import admin
from django.contrib.admin import register

from .models import Author, Article


@register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'email',)


@register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'body', 'author')

