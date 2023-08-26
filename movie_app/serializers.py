from rest_framework import serializers
from .models import Director, Movie, Review


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = 'id name'.split()


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'id starts text'.split()


class MovieSerializer(serializers.ModelSerializer):
    director = DirectorSerializer()
    filtered_reviews = ReviewSerializer(many=True)

    class Meta:
        model = Movie
        fields = 'id filtered_reviews description is_active director tags movie_name'.split()
