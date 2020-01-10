from rest_framework import serializers
from .models import Artist, Genre, Painting, Place, Event, Article, Comment


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ('is_master', 'name', 'photo', 'artist_date')


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('genre_name',)


class PaintingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Painting
        fields = ('title', 'photo', 'author', 'genres', 'datetime', 'painting_date')


class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = ('name', 'photo', 'address', 'latitude', 'longitude')


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('name', 'photo', 'place', 'paintings', 'artists', 'datetime', 'event_date')


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('title', 'places', 'paintings', 'artists', 'events', 'datetime', 'content')


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('article', 'parent', 'content', 'datetime')
