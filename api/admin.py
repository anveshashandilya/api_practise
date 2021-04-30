from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Podcast)
class PodcastAdmin(admin.ModelAdmin):
    list_display = ['id', 'podcast_name', 'podcast_narrator']

@admin.register(Song)
class PodcastAdmin(admin.ModelAdmin):
    list_display = ['id', 'song_name', 'song_artist']

@admin.register(Story)
class PodcastAdmin(admin.ModelAdmin):
    list_display = ['id', 'story_name', 'story_author', 'story_narrator']
