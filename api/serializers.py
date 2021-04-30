from rest_framework import serializers
from .models import *

class PodcastSerializer(serializers.Serializer):
    podcast_name = serializers.CharField(max_length = 70)
    podcast_narrator = serializers.CharField(max_length = 100)

    def create(self, validated_data):
        return Podcast.objects.create(**validated_data)

    def update(self, instance, validated_data):
        #instance parameter is the old value and validated_data is the new vale to be stored in db
        # print(instance.podcast_name)
        instance.podcast_name = validated_data.get('podcast_name', instance.podcast_name)
        # print(instance.podcast_name)

        # print(instance.podcast_narrator)
        instance.podcast_narrator = validated_data.get('podcast_narrator', instance.podcast_narrator)
        # print(instance.podcast_narrator)

        instance.save()
        return instance

class SongSerializer(serializers.Serializer):
    song_name = serializers.CharField(max_length = 70)
    song_artist = serializers.CharField(max_length = 100)

    def create(self, validated_data):
        return Song.objects.create(**validated_data)

    def update(self, instance, validated_data):
        #instance parameter is the old value and validated_data is the new vale to be stored in db
        # print(instance.song_name)
        instance.song_name = validated_data.get('song_name', instance.song_name)
        # print(instance.song_name)

        # print(instance.song_artist)
        instance.song_artist = validated_data.get('song_artist', instance.song_artist)
        # print(instance.song_artist)

        instance.save()
        return instance

class StorySerializer(serializers.Serializer):
    story_name = serializers.CharField(max_length = 70)
    story_author = serializers.CharField(max_length = 100)
    story_narrator = serializers.CharField(max_length = 100)

    def create(self, validated_data):
        return Story.objects.create(**validated_data)

    def update(self, instance, validated_data):
        #instance parameter is the old value and validated_data is the new vale to be stored in db
        # print(instance.song_name)
        instance.story_name = validated_data.get('story_name', instance.story_name)
        # print(instance.song_name)

        # print(instance.song_artist)
        instance.story_author = validated_data.get('story_author', instance.story_author)
        # print(instance.song_artist)

        instance.story_narrator = validated_data.get('story_narrator', instance.story_narrator)

        instance.save()
        return instance