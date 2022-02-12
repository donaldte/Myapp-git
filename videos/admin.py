from django.contrib import admin
from videos.models import Category, Videos

# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'organism', 'auteur', 'profil', 'cel']


@admin.register(Videos)
class VideosAdmin(admin.ModelAdmin):
    list_display = ['id', 'titleV', 'content', 'url', 'added']
