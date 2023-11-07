from django.contrib import admin
from .models import Category, Movie, IndexMovie, Comment


# Register your models here.

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['movie','comment_author','comment_date']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name', 'slug', 'creation_date', 'update_date']
    search_fields = ['name']


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ['title', 'releasedate', 'director', 'hours', 'creation_date', 'update_date']
    search_fields = ['title']


@admin.register(IndexMovie)
class IndexMovieAdmin(admin.ModelAdmin):
    list_display = ['name', 'sure', 'youtube_link']
    search_fields = ['name']
