from django.db import models

# Create your models here.
class Podcast(models.Model):
    podcast_name = models.CharField(max_length = 70)
    podcast_narrator = models.CharField(max_length = 100)

class Song(models.Model):
    song_name = models.CharField(max_length = 70)
    song_artist = models.CharField(max_length = 100)

class Story(models.Model):
    story_name = models.CharField(max_length = 70)
    story_author = models.CharField(max_length = 100)
    story_narrator = models.CharField(max_length = 100)
